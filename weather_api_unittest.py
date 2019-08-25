import unittest
import requests
from urllib import parse
from time import sleep

class WeatherTest(unittest.TestCase):
	def setUp(self):
		self.url = 'http://t.weather.sojson.com/api/weather/city/101030100'

	def test_weather_tianjin(self):
		r = requests.get(self.url)
		result = r.json()

		self.assertEqual(result['status'], 200)
		self.assertIn('success', result['message'])
		sleep(3)

	def test_weather_parm_error(self):
		data = {'city' : '999'}
		r = requests.get(self.url, params = data)

if __name__ == '__main__':
	unittest.main()