from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LookbookView.as_view(), name='collections'),
    path('<collection_id>/', views.show_lookbook, name='lookbook'),
    path('<collection_id>/<int:pk>', views.ShowSlideView.as_view(), name='slide'),
]
