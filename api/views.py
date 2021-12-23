from .models import *
from api.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

#Вывод кактегрий товаров № 1
@api_view(['GET'])
def CategoryList(request):
    Cat = Category.objects.all()
    serializer = CatSerializer(Cat, many=True)
    return Response(serializer.data)

#Список продуктов от id категорий №2
@api_view(['GET'])
def ProductList(request, category):
    products = Products.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#POST пополнение заказа) № 3
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_product(request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner_id = request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Общий список заявок № 4
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def Request_list(request):
        ListRequest = ListRequestdetail.objects.filter(owner_id = request.user.id)
        serializer = ListProductSerializer(ListRequest, many=True)
        return Response(serializer.data)

#№ 5
class RequestDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        ListRequest = ListRequestdetail.objects.filter(owner_id = request.user.id, pk=pk)
        serializer = ListProd(ListRequest, many=True)
        return Response(serializer.data)

    
    def put(self, request, pk):
        Requestdetail = ListRequestdetail.objects.get(owner_id = request.user.id, pk = pk)
        serializer = ListSerializer(Requestdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Requestdetail = ListRequestdetail.objects.get(owner_id = request.user.id, pk = pk)
        Requestdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)