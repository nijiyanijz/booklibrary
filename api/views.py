from django.shortcuts import render
from owner.models import Books
from customer.models import Carts
from rest_framework.views import APIView
from api.serializers import BookSerializer,UserCreationSerializer,CartSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from django.contrib.auth.models import User

class BooksView(APIView):
    def get(selfself,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Books.objects.get(id=id)
        serializer=BookSerializer(qs)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Books.objects.get(id=id)
        serializer=BookSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Books.objects.get(id=id)
        qs.delete()
        return Response({'message':'deleted'},status=status.HTTP_200_OK)





class UserCreationView(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()
    model=User

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class CartView(APIView):
    def get(selfself,request,*args,**kwargs):
        qs=Carts.objects.all()
        serializer=CartSerializer(qs,many=True)
        return Response(serializer.data)


   