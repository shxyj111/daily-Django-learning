from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

def login(request):
    # return HttpResponse("Hello World")
    # 如果在web下的templates文件下没有web文件夹嵌套，就用login.html,如果有web文件夹嵌套，就用web/login.html
    return render(request, 'web/login.html')
    # return redirect('https://www.baidu.com')

def url_list(request):

    urls = [
        # 'https://www.baidu.com',
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
