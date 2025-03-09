from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FoodItem, Meals


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields= '__all__'
        
        
class MealsSerializers(serializers.ModelSerializer):
    total_calories =  serializers.ReadOnlyField(source='total_calories')
    
    
    class Meta:
        model = Meals
        fields= '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username','passwors', 'email']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
            
        ) 
        return user      