from .models import FoodItem, Meals
from .serializers import FoodItemSerializer, MealsSerializers , UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt import TokenObtainPairView,TokenRefreshView
from django.contrib.auth.models import User


class FoodItemListCreateView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticated]
    
class MealsListCreateView(generics.ListCreateAPIView):
    serializer_class = MealsSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Meals.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]        


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        
    