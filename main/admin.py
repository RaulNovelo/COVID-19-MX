from django.contrib import admin
from .models import State
from .models import ConfirmedCase, SuspectedCase

admin.site.register(State)
admin.site.register(ConfirmedCase)
admin.site.register(SuspectedCase)