from django.urls import path
from . import views




urlpatterns = [
    path('recipes/', views.RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('signup/',views.user_create),
    # path('recipes/signin/', SigninCheck, name='signin-check'),
]