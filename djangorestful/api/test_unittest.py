import requests
import unittest

class UserTest(unittest.TestCase):
	def setUp(self):
		self.base_url = 'http://127.0.0.1:8000/users'
		self.auth = ('admin', 'admin')

	# def test_get_user(self):
	# 	r = requests.get(self.base_url + '/1/', auth = self.auth)
	# 	result = r.json()

	# 	self.assertEqual(result['username'], 'admin')
	# 	self.assertEqual(result['email'], 'dustinqiao@outlook.com')

	# def test_add_user(self):
	# 	form_data = {
	# 		'username':'qiao',
	# 		'email':'qiao@123.com',
	# 		'groups':'http://127.0.0.1:8000/groups/2/'
	# 	}
	# 	r = requests.post(self.base_url +'/', data = form_data, auth = self.auth)
	# 	result = r.json()

	# 	self.assertEqual(result['username'], 'qiao')

	# def test_update_user(self):
	# 	form_data = {'email':'qiao@890.com'}
	# 	r = requests.patch(self.base_url + '/4/', data = form_data, auth = self.auth)
	# 	result = r.json()

	# 	self.assertEqual(result['email'], 'qiao@890.com')

	# def test_delete_user(self):
	# 	r = requests.delete(self.base_url + '/5/', auth = self.auth)

	# 	self.assertEqual(r.status_code, 204)

	def test_no_auth(self):
		r = requests.get(self.base_url)
		result = r.json()
		print(result)
		# self.assertIn('not provided', result['detail'])

if __name__ == '__main__':
	unittest.main()