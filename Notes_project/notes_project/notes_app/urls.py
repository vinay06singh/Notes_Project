from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.create_note, name='create_note'),
    path('notes/<int:pk>/', views.fetch_note_by_id, name='fetch_note'),
    path('notes/search/', views.query_notes_by_title, name='query_notes_by_title'),
    path('notes/<int:pk>/update/', views.update_note, name='update_note'),
]
