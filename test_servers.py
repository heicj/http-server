from client import client
import unittest

class TestIt(unittest.TestCase):
	def test_1(self):
		self.assertEqual(client("hello"), b"hello")


if __name__ == '__main__':
	unittest.main()