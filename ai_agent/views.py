from django.shortcuts import render
from .assistant import get_agent_executor
from django.http import JsonResponse, HttpResponse
from .models import Chat
from utils.markdown_to_html import markdown_to_html


def ai_chat(request) -> HttpResponse:
    """
    Renders the AI chat interface.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered AI chat interface page.
    """

    return render(request, 'ai_agent/ai_chat.html')


def response(request):
    """Lida com uma requisição POST da interface de bate-papo,
    salvar a mensagem e a resposta no banco de dados e retorna um objeto JSON com a resposta.
    
    Se a requisição não for uma requisição POST,
    retornar uma resposta JSON com um status 400 e uma mensagem de erro.

    Args:
        request (Request): Requisição HTTP.
    """

    if request.method == 'POST':
        message = request.POST.get('message', '')
        
        agent = get_agent_executor()
        
        response_raw: str = agent.invoke(
            {
                'input': message
            }
        ).get('output', '')

        response = markdown_to_html(response_raw.strip())
        
        new_chat = Chat(
            message=message,
            response=response,
        )
        new_chat.save()
        return JsonResponse({'response': response})

    return JsonResponse({'response': 'Invalid request'}, status=400)
