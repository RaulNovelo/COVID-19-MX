from django.contrib import admin
from .models import State, Country
from .models import ConfirmedCase, SuspectedCase, DailyReport
from .mixins import ExportCsvMixin

@admin.register(Country)
class AdminCountry(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'latitude', 'longitude')
    actions = ['export_as_csv']

@admin.register(State)
class AdminState(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'latitude', 'longitude')
    actions = ['export_as_csv']

@admin.register(ConfirmedCase)
class AdminConfirmedCase(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('id', 'state_id', 'sex', 'age', 'symptoms_date', 'origin_country', 'healed')
    list_filter = ('symptoms_date', 'origin_country', 'healed', 'sex', 'state_id', 'age', )
    actions = ['export_as_csv']

@admin.register(SuspectedCase)
class AdminSuspectedCase(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('id', 'state_id', 'sex', 'age', 'symptoms_date', 'origin_country')
    list_filter = ('symptoms_date', 'origin_country', 'sex', 'state_id', 'age',)
    actions = ['export_as_csv']
    
@admin.register(DailyReport)
class AdminDailyReport(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('country', 'date', 'confirmed', 'deaths', 'recovered')
    list_filter = ('date',)
    ordering = ('country',)
    actions = ('export_as_csv',)