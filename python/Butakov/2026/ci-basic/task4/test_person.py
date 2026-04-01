import datetime
import unittest
from unittest.mock import patch

from person import Person


class PersonTestCase(unittest.TestCase):
    def test_init_sets_fields(self) -> None:
        person = Person(name="Анна", year_of_birth=1995, address="Екатеринбург")

        self.assertEqual(person.name, "Анна")
        self.assertEqual(person.yob, 1995)
        self.assertEqual(person.address, "Екатеринбург")

    def test_get_age(self) -> None:
        person = Person(name="Иван", year_of_birth=2000)
        mocked_now = datetime.datetime(2026, 3, 27)

        with patch("person.datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value = mocked_now
            self.assertEqual(person.get_age(), 26)

    def test_get_name(self) -> None:
        person = Person(name="Ольга", year_of_birth=1990)

        self.assertEqual(person.get_name(), "Ольга")

    def test_set_name(self) -> None:
        person = Person(name="Старое", year_of_birth=1990)

        person.set_name("Новое")

        self.assertEqual(person.get_name(), "Новое")

    def test_set_address(self) -> None:
        person = Person(name="Антон", year_of_birth=1988)

        person.set_address("Москва")

        self.assertEqual(person.get_address(), "Москва")

    def test_get_address(self) -> None:
        person = Person(name="Ира", year_of_birth=2001, address="Пермь")

        self.assertEqual(person.get_address(), "Пермь")

    def test_is_homeless_true_when_address_missing(self) -> None:
        person = Person(name="Аноним", year_of_birth=2001)

        self.assertTrue(person.is_homeless())

    def test_is_homeless_false_when_address_present(self) -> None:
        person = Person(name="Аноним", year_of_birth=2001, address="Казань")

        self.assertFalse(person.is_homeless())


if __name__ == "__main__":
    unittest.main()
