from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        unique_together = ['name']
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name

class ConfirmedCase(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    sex = models.SmallIntegerField() # https://en.wikipedia.org/wiki/ISO/IEC_5218
    age = models.SmallIntegerField()
    symptoms_date = models.DateField(blank=True, null=True)
    origin_country = models.CharField(max_length=30)
    healed = models.BooleanField()

class SuspectedCase(models.Model):
    """
    Hey! :P This model is super similar to ConfirmedCase. They could be mixed adding
    a column called Suspected but I decided to have two models to have
    consistency with goverment data.
    """
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    sex = models.SmallIntegerField()
    age = models.SmallIntegerField()
    symptoms_date = models.DateField(blank=True, null=True)
    origin_country = models.CharField(max_length=30)

class DailyReport(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    confirmed = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)