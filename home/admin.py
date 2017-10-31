# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Partes_maestro)
admin.site.register(Partes_electricas)
admin.site.register(Partes_mecanicas)
admin.site.register(Partes_carroceria)
