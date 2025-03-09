from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import FoodItemListCreateView, MealsListCreateView,RegisterUserView,LogoutView

urlpatterns = [
    path('food-items/', FoodItemListCreateView.as_view(), name='food-list'),
    path('meals/', MealsListCreateView.as_view(), name='meal-list'),
    path('register',RegisterUserView.as_view(),name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]