from django.db import models


class Chat(models.Model):
    message = models.CharField(max_length=100000)
    response = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Bate-papo'
        verbose_name_plural = 'Bate-papos'

    def __str__(self) -> str:
        """Retorna uma string que representa o objeto Chat

        Returns:
            str: A string que representa o objeto Chat
        """
        return f'Chat {self.id}: {self.message[:50]} -> {self.response[:50]}'
