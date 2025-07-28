from django.urls import path
from .views import events_page_view, event_detail_view, create_event, update_event, delete_event

urlpatterns = [
    path('', events_page_view, name='events'),
    path('<int:event_id>/', event_detail_view, name='event_detail'),
    path('create/', create_event, name='create_event'),
    path('update/<int:event_id>/', update_event, name='update_event'),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),
]
