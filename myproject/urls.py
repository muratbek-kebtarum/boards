from django.contrib import admin
from django.urls import path

from board import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('boards/<int:pk>', views.boards_topics, name='boards_topics'),
    path('admin/', admin.site.urls),
]
