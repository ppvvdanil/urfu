import unittest
from hw1_registration import app


def valid_payload():
    return {
        "email": "Dpopov25@yandex.ru",
        "phone": "8005553535",
        "name": "Danil",
        "address": "Address 1",
        "index": "624250",
        "comment": "Привет!",
    }


class RegistrationValidationTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["SECRET_KEY"] = "test-secret-key"
        self.client = app.test_client()

    def post(self, data):
        return self.client.post("/registration", data=data)

    def test_email_valid(self):
        response = self.post(valid_payload())
        self.assertEqual(response.status_code, 200)

    def test_email_invalid_format(self):
        data = valid_payload()
        data["email"] = "wrong-email"
        response = self.post(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.get_data(as_text=True))

    def test_phone_valid(self):
        response = self.post(valid_payload())
        self.assertEqual(response.status_code, 200)

    def test_phone_wrong_length(self):
        data = valid_payload()
        data["phone"] = "12345"
        response = self.post(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("phone", response.get_data(as_text=True))

    def test_name_valid(self):
        response = self.post(valid_payload())
        self.assertEqual(response.status_code, 200)

    def test_name_required(self):
        data = valid_payload()
        data["name"] = ""
        response = self.post(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.get_data(as_text=True))

    def test_address_valid(self):
        response = self.post(valid_payload())
        self.assertEqual(response.status_code, 200)

    def test_address_required(self):
        data = valid_payload()
        data["address"] = ""
        response = self.post(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("address", response.get_data(as_text=True))

    def test_index_valid(self):
        response = self.post(valid_payload())
        self.assertEqual(response.status_code, 200)

    def test_index_must_be_number(self):
        data = valid_payload()
        data["index"] = "abc"
        response = self.post(data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("index", response.get_data(as_text=True))

    def test_comment_optional_omitted(self):
        data = valid_payload()
        data.pop("comment")
        response = self.post(data)
        self.assertEqual(response.status_code, 200)

    def test_comment_optional_present(self):
        response = self.post(valid_payload())
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
