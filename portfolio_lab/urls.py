"""portfolio_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth import views as auth_views

from oddam_w_dobre_rece import views
from oddam_w_dobre_rece.forms import *
from oddam_w_dobre_rece.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view()),
    path('add-donation/', AddDonationView.as_view(), name='add-donation'),
    path('confirm-donation/', ConfirmDonationView.as_view(), name='confirm-donation'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(authentication_form=MyAuthForm), name='login'),  # wbudowane URLe w Django. Są np. /login, /logout itp.
    # path('login/', auth_views.LoginView.as_view(), name='login'),  # wbudowane URLe w Django. Są np. /login, /logout itp.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # wbudowane URLe w Django. Są np. /login, /logout itp.
    path('ajax/validate_username/', views.validate_username, name='validate-username'),  # wbudowane URLe w Django. Są np. /login, /logout itp.
]
