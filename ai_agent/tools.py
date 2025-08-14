from langchain.tools import Tool
from crm.models import Record
from django.db.models import Q
from .models import Chat


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


def get_past_context(*args, **kwargs):
    """Realiza uma busca no banco de dados pelas últimas 10 mensagens
    do chat atual, para serem usadas como contextos anteriores.

    Returns:
        str: Contexto de mensagens anteriores ou mensagem de nada encontrado
    """
    
    chat: list = Chat.objects.all().order_by('created_at')[:10]
    
    if not chat:
        return 'Nenhuma mensagem anterior encontrada.'
    
    context = '''
    Contexto Anterior:
    '''
    
    for message in chat:
        context += f'''
        Usuário: {message.message}
        Agente: {message.response}
        '''
        
    return context


def list_recent_records(limit: int = 5):
    """Retorna a lista dos registros mais recentes.
    
    Args:
        limit (int, optional): Número de registros a serem retornados. Padrão é 5.
    
    Returns:
        str: Lista de registros no formato:
            Nome: <nome>
            Email: <email>
            Telefone: <telefone>
            Endereço: <endereço>
            Cidade: <cidade>
            Estado: <estado>
            País: <país>
    """
    try:
        limit = int(limit)
        if limit < 1:
            limit = 1
    except (ValueError, TypeError):
        limit = 5

    if limit == 1:
        last_record = Record.objects.order_by('-created_at').first()
        return f'''
            Nome: {last_record.first_name} {last_record.last_name}
            Email: {last_record.email}
            Telefone: {last_record.phone}
            Endereço: {last_record.address}
            Cidade: {last_record.city}
            Estado: {last_record.state}
            País: {last_record.country}
        '''
    else:
        records = Record.objects.order_by('-created_at')[:limit]
        
        if not records:
            return 'Nenhum registro encontrado.'
        
        return '\n'.join(
            f'''
            Nome: {record.first_name} {record.last_name}
            Email: {record.email}
            Telefone: {record.phone}
            Endereço: {record.address}
            Cidade: {record.city}
            Estado: {record.state}
            País: {record.country}
            '''
            for record in records
        )


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
        ),
        Tool(
            name='List Recent Records',
            func=list_recent_records,
            description='Retorna a lista dos clientes (records) mais recentes.',
        ),
        Tool(
            name='Get Past Context',
            func=get_past_context,
            description='Retorna o contexto de mensagens anteriores.',
        ),
    ]
