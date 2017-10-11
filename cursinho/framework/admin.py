from django.contrib import admin

from cursinho.framework.models import RegisterPeriodo, RegisterSala, RegisterEscola, RegisterEnd, RegisterContatos
# Register your models here.
admin.site.register(RegisterPeriodo)
admin.site.register(RegisterSala)
admin.site.register(RegisterEscola)
admin.site.register(RegisterEnd)
admin.site.register(RegisterContatos)
