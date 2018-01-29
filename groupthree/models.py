# -*- coding: utf-8 -*-
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('500.00'))


class Juego(models.Model):
    juego_id = models.AutoField(primary_key=True)
    juego = models.CharField(max_length=250)

    def __str__(self):
        return self.juego


class Sala(models.Model):
    sala_id = models.AutoField(primary_key=True)
    juego = models.ForeignKey('groupthree.Juego', related_name='juegos')
    capacidad_maxima = models.IntegerField()
    cantidad_usuarios = models.IntegerField(default=0)
    es_publica = models.BooleanField(default=0)
    pozo_por_jugador = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    usuario_administrador = models.ForeignKey(User, related_name='+', null=True)

    def __str__(self):
        return self.sala_id

class SalaUsuario(models.Model):
    sala_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='+')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
