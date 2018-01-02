from django.db import models

# Create your models here.

from cursinho.accounts.models import User

class Alunos(User):

    @models.permalink
    def get_absolute_link(self):
        return ('alunos:details', (), {'slug': self.slug})

    class Meta:

        ordering=['name']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class FamiliaAluno(models.Model):

    name = models.CharField('Primeiro Nome', max_length=15, )
    parente = models.CharField('Parentesco', max_length=10)
    esc = models.CharField('Escolaridade', max_length=10)
    salario = models.FloatField('Salario')
    ref_aluno = models.OneToOneField(Alunos)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Familiar'
        verbose_name_plural = 'Familiares'
