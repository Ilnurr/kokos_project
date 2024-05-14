from django.contrib import admin
from aud.models import Currency, ExchangeRate

admin.site.register(Currency)
admin.site.register(ExchangeRate)