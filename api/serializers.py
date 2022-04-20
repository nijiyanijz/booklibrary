from rest_framework.serializers import ModelSerializer
from owner.models import Books
from customer.models import Carts
from django.contrib.auth.models import User

class BookSerializer(ModelSerializer):
    class Meta:
        model=Books
        fields='__all__'

class UserCreationSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(ModelSerializer):
    class Meta:
        model=Carts
        fields='__all__'
