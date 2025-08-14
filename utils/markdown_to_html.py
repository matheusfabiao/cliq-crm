from django.utils.safestring import mark_safe
from markdown import markdown


def markdown_to_html(text: str) -> str:
    """
    Converte uma string formatada em Markdown para HTML.
    Utiliza as extensões “extra” e “nl2br” para recursos adicionais.

    Args:
        text (str): A string a ser formatada em Markdown.

    Returns:
        str: A string formatada em HTML.
    """
    html = markdown(text, extensions=['extra', 'nl2br'])
    return mark_safe(html)
