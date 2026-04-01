import unittest

from freezegun import freeze_time

from good_day import app


class HelloWorldWithDayTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = app.test_client()

    @freeze_time("2026-03-23")  # Monday
    def test_can_get_correct_username(self) -> None:
        response = self.client.get("/hello-world/Алиса")
        text = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(text, "Привет, Алиса. Хорошего понедельника!")

    def test_can_get_correct_weekday(self) -> None:
        test_cases = [
            ("2026-03-23", "Хорошего понедельника"),
            ("2026-03-24", "Хорошего вторника"),
            ("2026-03-25", "Хорошей среды"),
            ("2026-03-26", "Хорошего четверга"),
            ("2026-03-27", "Хорошей пятницы"),
            ("2026-03-28", "Хорошей субботы"),
            ("2026-03-29", "Хорошего воскресенья"),
        ]

        for frozen_date, expected_greeting in test_cases:
            with self.subTest(date=frozen_date):
                with freeze_time(frozen_date):
                    response = self.client.get("/hello-world/Пользователь")
                    text = response.get_data(as_text=True)

                self.assertEqual(response.status_code, 200)
                self.assertIn(expected_greeting, text)

    @freeze_time("2026-03-23")  # Monday
    def test_username_that_looks_like_greeting_does_not_break_weekday(self) -> None:
        response = self.client.get("/hello-world/Хорошей среды")
        text = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(text, "Привет, Хорошей среды. Хорошего понедельника!")


if __name__ == "__main__":
    unittest.main()
