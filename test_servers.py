import unittest
from client import client

class TestIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(client("LF", "Test"), "Test")
		
	def test_2(self):
		self.assertEqual(client("LF", "This is a long string test"), "This is a long string test")
	
	def test_3(self):
		self.assertEqual(client("LF", ""), "")