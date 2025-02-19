"""
URL configuration for b_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
# from .views import CreateCheckoutSessionView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('sent/', views.sent, name='sent'),
    # path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),
    path('cancel/', TemplateView.as_view(template_name="cancel.html"), name='cancel')

]
