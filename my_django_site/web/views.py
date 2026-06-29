from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from web.models import Phone


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


# ========== 手机管理 CRUD ==========

def phone_list(request):
    """列表页：展示所有手机"""
    phones = Phone.objects.all()
    return render(request, 'web/phone_list.html', {'phones': phones})


def phone_add(request):
    """新增手机"""
    if request.method == 'POST':
        Phone.objects.create(
            name=request.POST.get('name'),
            brand=request.POST.get('brand'),
            price=request.POST.get('price'),
        )
        return redirect('phone_list')
    return render(request, 'web/phone_form.html')


def phone_edit(request, pk):
    """编辑手机"""
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        phone.name = request.POST.get('name')
        phone.brand = request.POST.get('brand')
        phone.price = request.POST.get('price')
        phone.save()
        return redirect('phone_list')
    return render(request, 'web/phone_form.html', {'phone': phone})


def phone_delete(request, pk):
    """删除手机"""
    phone = get_object_or_404(Phone, pk=pk)
    phone.delete()
    return redirect('phone_list')
