import unittest
import sys

# insert at 1, 0 is the script path (or '' in REPL)
# this is required for importing the app
sys.path.insert(1, '..')

from repos_app import app


class TestConfig(unittest.TestCase):
	def test_base_route(self):		
		response = app.test_client().get('/')
		assert response.status_code == 200
		

if __name__ == '__main__':
	unittest.main()