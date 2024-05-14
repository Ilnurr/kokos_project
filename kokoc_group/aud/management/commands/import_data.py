import json
import requests
from django.core.management.base import BaseCommand
from aud.models import Currency, ExchangeRate


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            data = response.json()
            for valute_code, valute_data in data['Valute'].items():
                currency, created = Currency.objects.get_or_create(
                    char_code=valute_code,  # Используйте char_code вместо code
                    defaults={
                        'name': valute_data['Name'],
                        'char_code': valute_data['Value']
                    }
                )
                if not created:
                    currency.value = valute_data['Value']
                    currency.save()
                
                ExchangeRate.objects.create(
                    currency=currency,
                    value=valute_data['Value'],
                    date=data['Date']
                )
            self.stdout.write(self.style.SUCCESS('Данные о валюте и обменном курсе успешно загружены!'))
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Ошибка сети: {e}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Ошибка при декодировании JSON-файла!'))