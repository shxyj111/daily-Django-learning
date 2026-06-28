from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Phone
from .serializers import PhoneSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    """手机 CRUD 接口
    GET    /api/phones/       - 列表
    POST   /api/phones/       - 新增
    GET    /api/phones/{id}/  - 详情
    PUT    /api/phones/{id}/  - 修改
    DELETE /api/phones/{id}/  - 删除
    """
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


@api_view(['GET'])
def api_overview(request):
    """API 总览"""
    return Response({
        'message': '手机管理 API',
        'endpoints': {
            'phones': '/api/phones/',
            'phone_detail': '/api/phones/<id>/',
            'overview': '/api/',
        }
    })
