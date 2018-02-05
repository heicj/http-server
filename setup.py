from setuptools import setup

setup(
	name= "http-server"
	description = "simple server"
	version = 0.1
	author = "Charlie Heiner"
	license = 'MIT'
	install_requires = ["io", "gevent", "socket", "sys", "gevent"]
)