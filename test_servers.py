from client import client
import unittest

class TestIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(client("LF", "Hello"), "Hello")
		
	def test_2(self):
		self.assertEqual(client("LF", "This is a long sentence to test response"), "This is a long sentence to test response")
		
	def tets_3(self):
		self.assertEqual(client("LF", ""), "")
	
	

