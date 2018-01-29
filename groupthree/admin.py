# -*- coding: utf-8 -*-
from django.contrib import admin
from groupthree.models import Juego


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('juego_id', 'juego')
    search_fields = ['juego']
