from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404






from example.models import User2
from example.models import Product

from example.models import Transaction
from example.models import Sale

from example.serializer import Inventory


from example.serializer import UserSerializer
from example.serializer import ProductSerializer
from example.serializer import UseridSerializer
from example.serializer import ProductidSerializer
from example.serializer import InventorySerializer
from example.serializer import InventoryidSerializer
from example.serializer import TransactionSerializer
from example.serializer import SaleSerializer


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#vistas de extra

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data,
        context = {'request':request}) 
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })



class ProductsList(APIView):
    
    def get(self, request, format=None):
        queryset = Product.objects.filter(delete=False)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            #print(request.user.id)
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(pk=id, delete=False)
        except Product.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ProductSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Product.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = ProductSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

class UsersList(APIView):
    
    def get(self, request, format=None):
        queryset = User.objects.filter(delete=False)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(pk=id, delete=False)
        except User.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = UserSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        User.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = UserSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#////////////////////////////////////////////////////////////////////////////////////////////////

class InventoriesList(APIView):
    
    def get(self, request, format=None):
        queryset = Inventory.objects.filter(delete=False)
        serializer = InventoriesList(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = InventorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class InventoriesDetail(APIView):
    def get_object(self, id):
        try:
            return Inventory.objects.get(pk=id, delete=False)
        except Inventory.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = InventorySerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Inventory.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = InventorySerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#//////////////////////////////////////////////////////////////////////////////////////////////

class TransactionsList(APIView):
    
    def get(self, request, format=None):
        queryset = Transaction.objects.filter(delete=False)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TransactionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class TransactionDetail(APIView):
    def get_object(self, id):
        try:
            return Transaction.objects.get(pk=id, delete=False)
        except Transaction.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = TransactionSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Transaction.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = TransactionSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#////////////////////////////////////////////////////////////////////////////////////

class SalesList(APIView):
    
    def get(self, request, format=None):
        queryset = Sale.objects.filter(delete=False)
        serializer = SaleSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SaleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SaleDetail(APIView):
    def get_object(self, id):
        try:
            return Sale.objects.get(pk=id, delete=False)
        except Sale.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Sale.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = SaleSerializer(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


