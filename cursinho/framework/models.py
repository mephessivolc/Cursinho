from django.db import models

# Create your models here.

class RegisterPeriodo(models.Model):
    name = models.CharField('Identificação', max_length=10)

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
        ordering = ['name']

class RegisterSala(models.Model):
    name = models.CharField('Nome', max_length=20)
    iden = models.CharField('Identificação', max_length=10)
    qtd = models.IntegerField('Capacidade Máxima')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['iden']

class RegisterEscola(models.Model):
    name = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'

class RegisterEnd(models.Model):
    end = models.CharField('Endereço', max_length=100, )
    numero = models.CharField('Numero', max_length=10, )
    cep = models.CharField('CEP', max_length=10, blank=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True)
    comp = models.CharField('Complemento', max_length=30, blank=True)
    idUser = models.IntegerField('idUser', blank=True, null=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

class RegisterContatos(models.Model):
    tel = models.CharField('Telefone', max_length = 10, blank=True, null=True)
    cel = models.CharField('Celular', max_length = 12, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)

    def __str__(self):
        return self.tel

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
