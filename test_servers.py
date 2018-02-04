import unittest
from client import client

class TestIt(unittest.TestCase):
	#test 1,2,3 work for echo server
	"""
	def test_1(self):
		self.assertEqual(client("LF", "Test"), "Test")
		
	def test_2(self):
		self.assertEqual(client("LF", "This is a long string test"), "This is a long string test")
	
	def test_3(self):
		self.assertEqual(client("LF", ""), "")
	"""
	
	#tests for step1 part of assignment getting http response
	#def test_4(self):
	#	"""uses key phase testOK to test get a 200 ok response"""
	#	self.assertEqual(client("LF", "testOK"), 'HTTP/1.1 200 OK')
		
	#def test_5(self):
	#	"""uses key phrase testError to check error response works"""
	#	self.assertEqual(client("LF", "testError"), 'HTTP/1.1 500 Internal Server Error')
		
	def test_6(self):
		"""test that request to server sends back the resource requested"""
		self.assertEqual(client("test"), "/")

