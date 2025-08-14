from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from utils.markdown_to_html import markdown_to_html

from .assistant import get_agent_executor
from .models import Chat


@login_required(login_url='login')
def ai_chat(request) -> HttpResponse:
    """
    Renders the AI chat interface.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered AI chat interface page.
    """

    return render(request, 'ai_agent/ai_chat.html')


@login_required(login_url='login')
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

        response_raw: str = agent.invoke({'input': message}).get('output', '')

        response = markdown_to_html(response_raw.strip())

        new_chat = Chat(
            message=message,
            response=response,
        )
        new_chat.save()
        return JsonResponse({'response': response})

    return JsonResponse({'response': 'Invalid request'}, status=400)
