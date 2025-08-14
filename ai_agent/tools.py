from langchain.tools import Tool
from crm.models import Record
from django.db.models import Q


def get_current_time(*args, **kwargs) -> str:
    """Retorna a hora atual no formato brasileiro (HH:MM)

    Returns:
        str: Data e hora atual no formato DD/MM/YYYY HH:MM
    """
    from datetime import datetime

    now = datetime.now()
    return now.strftime('%H:%M')


def get_current_date(*args, **kwargs) -> str:
    """Retorna a data atual no formato brasileiro (DD/MM/YYYY)

    Returns:
        str: Data atual no formato DD/MM/YYYY
    """
    from datetime import datetime

    now = datetime.now()
    return now.strftime("%d/%m/%Y")


def get_current_date_time(*args, **kwargs) -> str:
    """Retorna a data e hora atual no formato brasileiro (DD/MM/YYYY HH:MM)

    Returns:
        str: Data e hora atual no formato DD/MM/YYYY HH:MM
    """
    from datetime import datetime

    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M")


def get_record_by_name(name: str) -> str:
    """Retorna os dados do cliente (record),
    através de uma busca no banco de dados.

    Args:
        name (str): Nome do cliente

    Returns:
        str: Dados do cliente
    """

    name_split = name.strip().split()

    if len(name_split) == 1:
        # Busca se a parte está no first_name ou no last_name
        query = Q(first_name__icontains=name_split[0]) | Q(last_name__icontains=name_split[0])
    else:
        # Busca se ambas as partes aparecem nos campos corretos
        query = Q(first_name__icontains=name_split[0], last_name__icontains=name_split[-1]) | \
                Q(first_name__icontains=name_split[-1], last_name__icontains=name_split[0])

    record = Record.objects.filter(query).first()
    
    if record:
        return f'''
            Nome: {record.first_name} {record.last_name}
            Email: {record.email}
            Telefone: {record.phone}
            Endereço: {record.address}
            Cidade: {record.city}
            Estado: {record.state}
            País: {record.country}
        '''
    else:
        return 'Nenhum registro encontrado.'


def get_tools() -> list[Tool]:
    """Retorna uma lista de ferramentas para serem utilizadas no modelo de linguagem

    Returns:
        list[Tool]: Uma lista de ferramentas
    """

    return [
        Tool(
            name='Get Current Date',
            func=get_current_date,
            description='Retorna a data atual no formato brasileiro (DD/MM/YYYY)',
        ),
        Tool(
            name='Get Current Time',
            func=get_current_time,
            description='Retorna a hora atual no formato brasileiro (HH:MM)',
        ),
        Tool(
            name='Get Current Date Time',
            func=get_current_date_time,
            description='Retorna a data e hora atual no formato brasileiro (DD/MM/YYYY HH:MM)',
        ),
        Tool(
            name='Get Record By Name',
            func=get_record_by_name,
            description='Retorna os dados do cliente (record) pelo nome.',
        )
    ]
