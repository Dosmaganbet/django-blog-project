from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Админка [cite: 16]
    path('', include('catalog.urls')),        # Подключаем пути из приложения catalog
]