from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


def frontend(request):
    """前后端分离的前端入口页面"""
    return render(request, 'web/index.html')


def login(request):
    return render(request, 'web/login.html')


def url_list(request):
    urls = [
        'https://www.google.com',
        'https://www.bing.com',
        'https://www.yahoo.com',
        'https://www.yandex.com',
        'https://www.duckduckgo.com',
        'https://www.ask.com',
        'https://www.aol.com',
        'https://www.altavista.com',
    ]
    return render(request, 'web/url_list.html', {'urls': urls})


def phone_list(request):
    phones = [
        {'name': 'iPhone 15', 'brand': 'Apple', 'price': '7999'},
        {'name': 'Galaxy S24', 'brand': 'Samsung', 'price': '5999'},
        {'name': 'Pixel 8', 'brand': 'Google', 'price': '4999'},
        {'name': 'Mate 60', 'brand': 'Huawei', 'price': '6999'},
        {'name': 'Xiaomi 14', 'brand': 'Xiaomi', 'price': '3999'},
    ]
    return render(request, 'web/phone_list.html', {'phones': phones})
