from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.product, name='product'),
    path('category/<int:category_id>/', views.category, name='category'),
]