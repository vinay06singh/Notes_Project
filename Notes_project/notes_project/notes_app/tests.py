from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Note

class NoteTests(APITestCase):
    def test_create_note(self):
        url = reverse('create_note')
        data = {'title': 'Test Note', 'body': 'This is a test note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_note_by_id(self):
        note = Note.objects.create(title="Test", body="Body")
        url = reverse('fetch_note', kwargs={'pk': note.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_query_notes_by_title(self):
        Note.objects.create(title="First", body="First body")
        Note.objects.create(title="Second", body="Second body")
        url = reverse('query_notes_by_title')
        response = self.client.get(f'{url}?title=First')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_note(self):
        note = Note.objects.create(title="Test", body="Body")
        url = reverse('update_note', kwargs={'pk': note.id})
        data = {'title': 'Updated Title', 'body': 'Updated Body'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
