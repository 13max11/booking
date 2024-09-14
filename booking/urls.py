from booking import views
from django.urls import path


urlpatterns = [
    path('rooms/', views.rooms_list, name='room-list')
]
