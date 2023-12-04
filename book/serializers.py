from rest_framework import serializers
from . import models
from account import models as account_models


# class CardTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Cardtype
#         fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = models.Street
        fields = [
            'id',
            'street',
            'city'
        ]
<<<<<<< HEAD

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.CustomUser
        fields = '__all__'

     
class CitySerializer(serializers.ModelSerializer):   

    class Meta:
        model = models.City
        fields = '__all__'      

class StreetSerializer(serializers.ModelSerializer):   
    city=CitySerializer()
    class Meta:
        model = models.Street
        fields = '__all__'      

class AddressSerializer(serializers.ModelSerializer):   
    streetname=StreetSerializer()
    class Meta:
        model = models.Address
        fields = '__all__'    


class OrderSerializer(serializers.ModelSerializer):
    customer_user=CustomUserSerializer()
    to_address=AddressSerializer()
    
    class Meta:
        model = models.Order
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserCard
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Payment
        fields = '__all__'
=======
>>>>>>> 049dd5a9771965afa8e66fc8d103aee34b35e5be
