from django.db import models

# Create your models here.

from cursinho.accounts.models import User

class Alunos(User):

    ref = models.CharField('Referencia', max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
