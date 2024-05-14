from django.db import models

class Currency(models.Model):
    char_code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = ('Валюта')
        verbose_name_plural = ('Валюты')

        def __str__(self):
            return f'{self.char_code} - {self.name}'

class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateTimeField()
    value = models.FloatField()

    class Meta:
        verbose_name = ('Курс валют')
        verbose_name_plural = ('Курс валют')
        unique_together = ['currency', 'date']

    def __str__(self):
        return f'{self.currency}: {self.date} ({self.value})'