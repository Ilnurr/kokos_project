from django.http import JsonResponse
from .models import ExchangeRate

def show_exchange_rates(request):
    # Получение всех объектов ExchangeRate
    queryset = ExchangeRate.objects.all()
    
    # Получение параметров запроса
    char_code = request.GET.get('char_code')
    date = request.GET.get('date')
    if char_code:
        queryset = queryset.filter(currency__char_code=char_code.upper())
    if date:
        queryset = queryset.filter(date__date=date)
    return JsonResponse(
        list(queryset.values('currency__char_code', 'date', 'value')),
        safe=False
    )


