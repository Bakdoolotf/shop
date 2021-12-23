from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()
class Userserializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', ]


#Категрия
class CatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)

#Продукт
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'content', 'price','volume', 'time_create', 'category']

#Список истории заказов
class ListProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time_create = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True)
    is_finish = serializers.BooleanField(default=False)
    quantity = serializers.IntegerField()
    summ = serializers.IntegerField()
    address = serializers.CharField()
    phone_number = serializers.IntegerField()
    owner = Userserializers(read_only=True)

#Заказ
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListRequestdetail
        fields = ['id','product','quantity', 'summ', 'is_finish', 'address', 'phone_number',  'owner']



class ListProd(serializers.Serializer):
    id = serializers.IntegerField()
    product = ProductSerializer()
    quantity = serializers.IntegerField()
    summ = serializers.IntegerField()
    time_create = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True)
    is_finish = serializers.BooleanField(default=False)
    address = serializers.CharField()
    phone_number = serializers.IntegerField()
    owner = Userserializers(read_only=True)

    def create(self, validated_data):
        return ListRequestdetail.objects.create(**validated_data)