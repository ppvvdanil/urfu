import unittest

from decoder import decrypt


class DecryptTestCase(unittest.TestCase):
    def test_cases_with_single_dots(self) -> None:
        test_cases = [
            ("абра-кадабра.", "абра-кадабра"),
            (".", ""),
            ("1..2.3", "23"),
            ("абр......a.", "a"),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)

    def test_cases_with_double_dots(self) -> None:
        test_cases = [
            ("абраа..-кадабра", "абра-кадабра"),
            ("абра--..кадабра", "абра-кадабра"),
            ("абра........", ""),
            ("1.......................", ""),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)

    def test_cases_with_mixed_dots(self) -> None:
        test_cases = [
            ("абраа..-.кадабра", "абра-кадабра"),
            ("абрау...-кадабра", "абра-кадабра"),
        ]

        for encrypted, expected in test_cases:
            with self.subTest(encrypted=encrypted):
                self.assertEqual(decrypt(encrypted), expected)


if __name__ == "__main__":
    unittest.main()
