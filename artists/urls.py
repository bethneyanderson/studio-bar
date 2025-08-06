from django.urls import path
from .views import (
    artists_list_view,
    create_artist_view, update_artist_view, delete_artist_view
)

urlpatterns = [
    path('', artists_list_view, name='artists_list'),
    path('create/', create_artist_view, name='create_artist'),
    path('update/<int:artist_id>/', update_artist_view, name='update_artist'),
    path('delete/<int:artist_id>/', delete_artist_view, name='delete_artist'),
]
