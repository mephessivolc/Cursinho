import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)
from django.conf import settings

from cursinho.framework.models import RegisterEnd

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou os '
            'seguintes caracteres: @ . + - _', 'invalid')],
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, )
    is_active = models.BooleanField('Está ativo?', default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    slug = models.SlugField('Atalho', blank=True)

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
