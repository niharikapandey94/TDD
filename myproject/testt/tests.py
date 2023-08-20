from django.test import TestCase


from django.test import TestCase
from django.urls import reverse

class WeatherViewTest(TestCase):

    def test_get_valid_city(self):
        response = self.client.get(reverse('weather_detail', kwargs={'city': 'San Francisco'}))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'temperature': 14, 'weather': 'Cloudy'})

    def test_get_invalid_city(self):
        response = self.client.get(reverse('weather_detail', kwargs={'city': 'InvalidCity'}))
        self.assertEqual(response.status_code, 404)

    def test_create_weather_data(self):
        new_weather_data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Sunny'}
        response = self.client.post(reverse('weather_list'), data=new_weather_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(str(response.content, encoding='utf8'), new_weather_data)

    def test_update_weather_data(self):
        updated_weather_data = {'temperature': 28, 'weather': 'Hot'}
        response = self.client.put(reverse('weather_detail', kwargs={'city': 'San Francisco'}),
                                   data=updated_weather_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), updated_weather_data)

    def test_delete_weather_data(self):
        response = self.client.delete(reverse('weather_detail', kwargs={'city': 'Los Angeles'}))
        self.assertEqual(response.status_code, 204)
