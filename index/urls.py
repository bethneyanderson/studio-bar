from django.urls import path, include
from .views import (
    home_page_view, artists_list_view, 
    create_artist_view, update_artist_view, delete_artist_view
)

urlpatterns = [
    path('', home_page_view, name='home'),
    path('artists/', artists_list_view, name='artists_list'),
    path('artists/create/', create_artist_view, name='create_artist'),
    path('artists/update/<int:artist_id>/', update_artist_view, name='update_artist'),
    path('artists/delete/<int:artist_id>/', delete_artist_view, name='delete_artist'),
    path('summernote/', include('django_summernote.urls')),
]