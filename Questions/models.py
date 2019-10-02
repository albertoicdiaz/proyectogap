from django.db import models
from Questions.defines import *
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Cont(models.Model):
    cont = models.IntegerField(default=0)

class Question(models.Model):
    question = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=3, choices=DOMINIO_CHOICE)

    def __str__(self):
        return "%s, %s" % (self.question, self.type)

class Empresa(models.Model):
    name = models.CharField(max_length=100)
    n_workers = models.IntegerField()

    def __str__(self):
        return "Nombre: %s" % (self.name)

class Personal(models.Model):
    usuario_personal = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=3, choices=POSITION_CHOICE)
    status = models.BooleanField(default=True)
    initial = models.DateField()
    finish = models.DateField()
    company = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return "usuario: %s ,Cargo: %s" % (self.usuario_personal, self.position)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    usuario_choice = models.ForeignKey(Personal, on_delete=models.CASCADE)
    answer = models.CharField(max_length = 10)
    company = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['question', 'usuario_choice']

    def __str__(self):
        return ":%s, answer: %s user: %s" % (self.question, self.answer, self.usuario_choice)

class Analisis(models.Model):
    type = models.CharField(max_length=50)
    total_t = models.FloatField(max_length=50)
    total_f = models.FloatField(max_length=50)
    percentaje_t = models.FloatField(max_length=50)
    percentaje_f = models.FloatField(max_length=50)
    date_analysis = models.DateField(default=timezone.now)