from django.shortcuts import render
from .models import Price
def news_home(request):
    price = Price.objects.all()
    return render(request, 'news/news_home.html', {'price':price})
