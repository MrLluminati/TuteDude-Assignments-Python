import unittest

from app import app, registered_users


class RegistrationFormTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        registered_users.clear()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Registration Form", response.data)

    def test_invalid_form_submission_returns_errors(self):
        response = self.client.post("/register", data={
            "name": "",
            "email": "invalid-email",
            "phone": "123",
            "course": "",
            "password": "123",
            "confirm_password": "456",
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Name is required.", response.data)
        self.assertIn(b"Enter a valid email address.", response.data)
        self.assertIn(b"Phone number must contain exactly 10 digits.", response.data)
        self.assertIn(b"Passwords do not match.", response.data)

    def test_valid_form_submission_succeeds(self):
        response = self.client.post("/register", data={
            "name": "Abhijeet Kumar",
            "email": "abhijeet@example.com",
            "phone": "9876543210",
            "course": "Flask",
            "password": "secret123",
            "confirm_password": "secret123",
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Registration Successful", response.data)
        self.assertEqual(len(registered_users), 1)


if __name__ == "__main__":
    unittest.main()
