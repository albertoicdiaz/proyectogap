from django.contrib import admin
from Questions.models import Question, Choice, Personal, Analisis, Empresa

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Personal)
admin.site.register(Analisis)
admin.site.register(Empresa)
