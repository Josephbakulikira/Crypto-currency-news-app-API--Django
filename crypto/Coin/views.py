from django.shortcuts import render

import requests
import json
# Create your views here.
def Home(request):

    #crypto news
    news_requests = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    news = json.loads(news_requests.content)
    #crypto price
    price_requests = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD,EUR")
    price = json.loads(price_requests.content)

    context = {"news": news, "price":price}

    return render(request, 'Coin/Home.html', context)
