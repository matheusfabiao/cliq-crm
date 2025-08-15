import os
from pathlib import Path

import pandas as pd
from django.apps import apps
from django.db.utils import IntegrityError


def import_records():
    Record = apps.get_model('crm', 'Record')

    # Caminho para o arquivo de dados
    BASE_DIR = Path(__file__).resolve().parent.parent.parent  # volta até a raiz do projeto
    file_path = BASE_DIR / "crm" / "utils" / "data" / "clientes.xlsx"

    if not os.path.exists(file_path):
        print(f'Arquivo {file_path} não encontrado.')
        return

    try:
        # Ler o arquivo
        if file_path.lower().endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        elif file_path.lower().endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            print('Formato de arquivo não suportado.')
            return

        # Verificar se as colunas necessárias existem
        required_columns = {
            'Nome',
            'Email',
            'Telefone',
            'Endereço',
            'Cidade',
            'Estado',
            'País',
        }
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            print(f'Colunas faltando no arquivo: {missing}')
            return

        df = df.rename(
            columns={
                'Nome': 'nome_completo',
                'Email': 'email',
                'Telefone': 'phone',
                'Endereço': 'address',
                'Cidade': 'city',
                'Estado': 'state',
                'País': 'country',
            }
        )

        # Separar nome completo em first_name e last_name
        def split_name(full_name):
            if pd.isna(full_name) or not str(full_name).strip():
                return '', ''

            slices = str(full_name).strip().split()
            if not slices:
                return '', ''

            first_name = slices[0]
            last_name = ' '.join(slices[1:]) if len(slices) > 1 else ''
            return first_name, last_name

        # Aplicar a função de separação de nomes de forma mais segura
        df[['first_name', 'last_name']] = df['nome_completo'].apply(
            lambda x: pd.Series(split_name(x))
        )

        records = df.to_dict(orient='records')

        records_created = 0
        records_updated = 0
        records_failed = 0

        for record_data in records:
            try:
                # Preparar os dados para o modelo
                defaults = {
                    'first_name': record_data.get('first_name', ''),
                    'last_name': record_data.get('last_name', ''),
                    'phone': record_data.get('phone', ''),
                    'address': record_data.get('address', ''),
                    'city': record_data.get('city', ''),
                    'state': record_data.get('state', ''),
                    'country': record_data.get('country', ''),
                }

                # Validar e-mail (campo obrigatório)
                email = record_data.get('email')
                if not email or pd.isna(email):
                    print('Registro sem e-mail - ignorando')
                    records_failed += 1
                    continue

                # Usar email como chave única
                obj, created = Record.objects.update_or_create(
                    email=email, defaults=defaults
                )

                if created:
                    records_created += 1
                else:
                    records_updated += 1

            except IntegrityError as e:
                print(
                    f"Erro ao importar cliente {record_data.get('email')}: {str(e)}"
                )
                records_failed += 1
            except Exception as e:
                print(
                    f"Erro inesperado com {record_data.get('email')}: {str(e)}"
                )
                records_failed += 1

        print(
            f'Importação concluída: {records_created} novos, {records_updated} atualizados, {records_failed} erros.'
        )

    except Exception as e:
        print(f'Erro ao processar o arquivo: {str(e)}')
