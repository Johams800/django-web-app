"""MidtermProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [
    path('', views.details, name='home'),
    path('home/', views.details, name='home'),
    path('create/', views.CreateCustomerView.as_view(), name='create'),
    path('edit/<int:id>', views.EditCustomerView.as_view(), name='edit'),
    path('add_trans/<int:fk>', views.AddTransaction.as_view(), name='add_trans'),
    path('add_account/<int:fk>', views.AddAccountView.as_view(), name='add_account'),
    path('edit_account/<int:id>', views.EditAccountView.as_view(), name='edit_account'),
]
