from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('category/', views.CategoriesView.as_view(), name='categories'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
    path('<product_id>/',
        views.product_detail,
        name='product_detail'),
]
