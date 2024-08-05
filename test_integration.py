import requests
import unittest

class TestIntegration(unittest.TestCase):
    def test_frontend_backend_integration(self):
        # URL of the frontend service
        frontend_url = 'http://localhost:8080/'

        # Make a request to the frontend service
        response = requests.get(frontend_url)

        # Verify the response
        self.assertIn('Hello from the Backend!', response.text)

if __name__ == '__main__':
    unittest.main()
