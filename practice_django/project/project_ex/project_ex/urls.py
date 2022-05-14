from django.contrib import admin
from django.urls import path, include
from app_ex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_ex/', include('app_ex.urls')),
    path('', views.weather, name='weather'),
]
