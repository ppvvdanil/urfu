import unittest
from typing import Any, cast
from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):
    def test_error_is_ignored(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                _ = 1 / 0
        except Exception as exc:
            self.fail(f'Exception should be suppressed, got: {exc}')

    def test_unexpected_error_is_raised(self):
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors({TypeError}):
                _ = 1 / 0

    def test_inner_propagated_and_outer_ignored(self):
        try:
            with BlockErrors({TypeError}):
                with BlockErrors({ZeroDivisionError}):
                    _ = cast(Any, 1) / cast(Any, '0')
        except Exception as exc:
            self.fail(f'Exception should be suppressed by outer context, got: {exc}')

    def test_child_errors_are_ignored(self):
        try:
            with BlockErrors({ArithmeticError}):
                _ = 1 / 0
        except Exception as exc:
            self.fail(f'Child exception should be suppressed, got: {exc}')


if __name__ == '__main__':
    unittest.main()
