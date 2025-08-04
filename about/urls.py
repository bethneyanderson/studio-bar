from django.urls import path
from .views import about_page_view, edit_about_view

urlpatterns = [
    path('', about_page_view, name='about'),
    path('edit/', edit_about_view, name='edit_about'),
]
