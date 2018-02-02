from client import client
import unittest

class TestIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(client("LF", "Hello"), "Hello")

