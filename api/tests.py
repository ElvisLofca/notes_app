from django.test import TestCase

# Create your tests here.
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status


class RoutesTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_get_routes(self):
        """
        Ensure we can get a list of 5 routes object.
        """
        url = reverse('routes')
        response = self.client.get(url, format='json')
        print("test_get_routes", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)


class NotesTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_get_notes(self):
        """
        Ensure we can get a list of notes.
        """
        url = reverse('notes')
        response = self.client.get(url, format='json')
        print("test_get_notes", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 0)


    def test_create_notes_with_data(self):
        """
        Ensure we can create a notes.
        """
        url = reverse('notes')
        response = self.client.post(url, data={'body': 'Note 1'}, follow=True)
        print("test_create_notes_with_data", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data, True)


    def test_create_notes_without_data(self):
        """
        Ensure we do not can create a notes with no body.
        """
        url = reverse('notes')
        response = self.client.post(url, data={'body': ''}, follow=True)
        print("test_create_notes_without_data", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)