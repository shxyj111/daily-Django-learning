from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from web import views
from web.api_views import PhoneViewSet, api_overview

# DRF 路由
router = DefaultRouter()
router.register(r'phones', PhoneViewSet, basename='phone')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', api_overview, name='api-overview'),
    # 原有页面（可选保留）
    path('login/', views.login),
    path('url_list/', views.url_list),
    path('phone_list/', views.phone_list),
    path('', views.frontend, name='frontend'),
]
