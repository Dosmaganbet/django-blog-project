from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Настройка API
router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    
    # ВОТ ЭТА СТРОЧКА ДОБАВИЛАСЬ:
    path('about/', views.about, name='about'),

    path('api/', include(router.urls)),
]