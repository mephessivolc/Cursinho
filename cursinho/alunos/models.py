from django.db import models

# Create your models here.

class RegisterAluno(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email')
    sex = models.CharField('Sexo', max_length=1)
    dCronicas = models.CharField('Doenças Crônicas', max_length=30)
    estcivil = models.CharField('Estado Civil', max_length=1)
    qtdfilhos = models.IntegerField('Quantidade de Filhos',)
    concEnsMed = models.CharField('Conclusão do Ensino Médio', max_length=3)
    bolsaEnsMed = models.CharField('Bolsa do Ensino Médio', max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['name']

class RegisterFamiliares(models.Model):
    firstname = models.CharField('Primeiro Nome', max_length=35)
    parent = models.CharField('Parentesco', max_length=15)
    profissao = models.CharField('Profissão', max_length=15)
    salario = models.FloatField('Salário', default=0)
    escolaridade = models.CharField('Escolaridade', max_length=10)

    class Meta:
        verbose_name = 'Familiar'
        verbose_name_plural = 'Familiares'

class RegisterGastoCasa(models.Model):
    moradia = models.FloatField('Moradia', default=0)
    alim = models.FloatField('Alimentação', default=0)
    agua = models.FloatField('Agua', default=0)
    tel = models.FloatField('Telefonia', default=0)
    trans = models.FloatField('Transportes', default=0)
    educ = models.FloatField('Educação', default=0)
    saude = models.FloatField('Saude', default=0)
    iptu = models.FloatField('IPTU', default=0)
    ipva = models.FloatField('IPVA', default=0)

    class Meta:
        verbose_name = 'Gasto FAamiliar'
        verbose_name_plural = 'Gastos Familiares'
