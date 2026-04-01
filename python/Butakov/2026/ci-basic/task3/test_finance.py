import unittest

from finance import app, storage


class FinanceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app.config["TESTING"] = True
        cls.client = app.test_client()
        cls.initial_storage = {
            "20240110": [100, 50],
            "20240210": [200],
            "20250101": [300],
        }

    def setUp(self) -> None:
        storage.clear()
        for day, values in self.initial_storage.items():
            storage[day] = values.copy()

    def test_add_endpoint_returns_ok_for_valid_data(self) -> None:
        response = self.client.get("/add/20240311/700")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "OK")
        self.assertEqual(storage["20240311"], [700])

    def test_add_endpoint_appends_to_existing_date(self) -> None:
        response = self.client.get("/add/20240110/25")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(storage["20240110"], [100, 50, 25])

    def test_add_endpoint_fails_for_invalid_date(self) -> None:
        with self.assertRaises(ValueError):
            self.client.get("/add/2024-01-10/10")

    def test_calculate_year_endpoint_returns_year_total(self) -> None:
        response = self.client.get("/calculate/2024")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "350")

    def test_calculate_year_endpoint_returns_zero_for_absent_year(self) -> None:
        response = self.client.get("/calculate/2030")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "0")

    def test_calculate_year_endpoint_returns_zero_for_empty_storage(self) -> None:
        storage.clear()

        response = self.client.get("/calculate/2024")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "0")

    def test_calculate_month_endpoint_returns_month_total(self) -> None:
        response = self.client.get("/calculate/2024/2")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "200")

    def test_calculate_month_endpoint_returns_zero_for_absent_month(self) -> None:
        response = self.client.get("/calculate/2024/12")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "0")

    def test_calculate_month_endpoint_returns_zero_for_empty_storage(self) -> None:
        storage.clear()

        response = self.client.get("/calculate/2024/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "0")


if __name__ == "__main__":
    unittest.main()
