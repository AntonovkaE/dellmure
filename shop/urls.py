"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.contrib.flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    # path('lookbook/', include('lookbook.urls')),
    path('about/', include('django.contrib.flatpages.urls')),
    path('', include('my_shop.urls')),


]
urlpatterns += [
    path('about/us/', views.flatpage, {'url': '/about-us/'}, name='about'),
    path('about/contacts/', views.flatpage, {'url': '/contacts/'}, name='contacts'),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
