"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

# from django.contrib.auth import views as auth_views

from mysite.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    # redirect_authenticated_user: A boolean that controls whether or not
    # authenticated users accessing the login page will be redirected as if
    # they had just successfully logged in.
    # path('login/',
    #      auth_views.LoginView.as_view(redirect_authenticated_user=True),
    #      name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # path('password-reset', auth_views.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password-change', auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
]
