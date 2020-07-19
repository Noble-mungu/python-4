import unittest

from app.models import User

class userTest(unittest.TestCase):
	def setUp(self):
		self.new_user = user{username='Noble',password = 'foody'}

	def test_password_setter(self):
		self.assertTrue(self.new_user.password is not None)

	def test_no_access_password(self):
		with self.assertRaise(AttributeError):
			self.new_user.password
    def test_password_verificatiom(self):
    	self.assertTrue(self.new_user.verify('foody'))
    	
