from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import SignupForm
from unittest.mock import patch
from .models import Match, Reservation
from django.contrib.messages import get_messages

User = get_user_model()

class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')

    def test_register_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post_valid(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
        }
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('connexion'))
        self.assertTrue(User.objects.filter(username='testuser').exists())


# ================================================================================

class ReservationBilletViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.match = Match.objects.create(date='2025-07-01', heure='18:00')
        self.url = reverse('reservation')  # Assure-toi que ce nom est correct dans urls.py

    @patch('FootZonePlusApp.views.reserver_meilleure_place')  # modifie le chemin si nécessaire
    def test_reservation_billet_post_valide(self, mock_reserver):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.url, {
            'match_id': str(self.match.id),
            'type_place': ['VIP']
        })
        self.assertRedirects(response, reverse('profil'))
        mock_reserver.assert_called_once_with(self.user, str(self.match.id), ['VIP'])

    def test_reservation_billet_post_invalide(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.url, {
            'match_id': '',
            'type_place': []
        }, follow=True)
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("Veuillez sélectionner un match et un type de place.", messages)
        self.assertRedirects(response, reverse('profil'))

    def test_reservation_billet_get(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reserverBillet.html')