import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)
from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):

    type_cargo = (
        ('', 'Nenhum'),
        ('Prof', 'Professor'),
        ('Plan', 'Plantonista'),
        ('Aux', 'Auxiliar'),
    )
    type_com = (
        ('', 'Nenhum'),
        ('Adm', 'Administração'),
        ('Ped', 'Pedagógica'),
        ('Cul', 'Cultural'),
    )

    username = models.CharField(
        'Usuário', max_length=30, unique=True,
        # validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
        #     'O nome de usuário só pode conter letras, digitos ou os '
        #     'seguintes caracteres: @ . + - _', 'invalid')],
    )
    email = models.EmailField('E-mail', unique=True, )
    name = models.CharField('Nome', max_length=100, )
    cel = models.CharField('Celular', max_length=16, )
    is_active = models.BooleanField('Está ativo?', default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    slug = models.SlugField('Atalho', blank=True)
    end = models.CharField('Endereço', max_length=100, default='')
    num_end = models.CharField('Numero', max_length=10, default='')
    bairro_end = models.CharField('Bairro', max_length=10, default='')
    comp_end = models.CharField('Complemento', max_length=30, default='', blank=True, null=True)
    cep_end = models.CharField('CEP', max_length=10, default='', blank=True, null=True)
    cargo = models.CharField('Cargo', max_length=10, choices=type_cargo, default='', blank=True)
    com = models.CharField('Comissão', max_length=10, choices=type_com, default='', blank=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    NAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    @models.permalink
    def get_absolute_link(self):
        return ('accounts:details', (), {'slug': self.slug})

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering=['name']
