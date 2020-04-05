from django.contrib import admin
from .models import State
from .models import ConfirmedCase, SuspectedCase

admin.site.register(State)
@admin.register(ConfirmedCase)
class AdminConfirmedCase(admin.ModelAdmin):
    list_display = ('id', 'state_id', 'sex', 'age', 'symptoms_date', 'origin_country', 'healed')
    list_filter = ('symptoms_date', 'origin_country', 'healed', 'sex', 'state_id', 'age', )

@admin.register(SuspectedCase)
class AdminSuspectedCase(admin.ModelAdmin):
    list_display = ('id', 'state_id', 'sex', 'age', 'symptoms_date', 'origin_country')
    list_filter = ('symptoms_date', 'origin_country', 'sex','state_id',  'age', )