
from django.contrib import admin
from django.urls import path,include
from accounts.views import UserRegisterView
from .views import SearchView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('django.contrib.auth.urls')),
    path('search/', SearchView.as_view(), name='search'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('auth/',include('accounts.urls',namespace='accounts')),
    path('',include('posts.urls',namespace='post')),

]
