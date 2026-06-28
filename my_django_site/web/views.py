from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

def login(request):
    # return HttpResponse("Hello World")
    return render(request, 'web/login.html')
    # return redirect('https://www.baidu.com')
