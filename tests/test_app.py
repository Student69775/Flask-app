import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client"""
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        """Test if the home page loads correctly"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        """Test if the about page loads correctly"""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        """Test if the contact page loads correctly"""
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
