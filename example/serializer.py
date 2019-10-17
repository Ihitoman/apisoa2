from rest_framework import routers, serializers

from django.contrib.auth.models import User

from example.models import User2
from example.models import Product

from example.models import Inventory
from example.models import Transaction

from example.models import Sale


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class UseridSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username')

class ProductnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name')

class InventorySerializer(serializers.ModelSerializer):
    #usuarioI = UseridSerializer(many=True)
    #productoI = ProductidSerializer(many=True)
    class Meta:
        model = Inventory
        fields = ('__all__')

class InventoryviewSerializer(serializers.ModelSerializer):
    usuario = UseridSerializer(many=True, read_only=True)
    producto = ProductnameSerializer(many=True, read_only=True)
    class Meta:
        model = Inventory
        fields = ('quantity', 'usuario', 'producto')
        #fields = ('__all__')


class InventoryidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id')

class TransactionSerializer(serializers.ModelSerializer):
    #inventario = InventoryidSerializer(many=True)
    class Meta:
        model = Transaction
        fields = ('__all__')

class SaleSerializer(serializers.ModelSerializer):
    #usuarioI = UseridSerializer(many=True)
    #productoI = ProductidSerializer(many=True)
    class Meta:
        model = Sale
        fields = ('__all__')

