from .views import cart_detail
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path("add/", views.cart_add, name='cart_add'),
    path("remove/<int:size_id>/", views.cart_remove, name='cart_remove')
]
