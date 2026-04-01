import unittest
import io
import sys
from redirect import Redirect


class TestRedirect(unittest.TestCase):
    def test_redirect_both_streams(self):
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()

        with Redirect(stdout=stdout_buffer, stderr=stderr_buffer):
            print('hello stdout')
            raise ValueError('hello stderr')

        self.assertIn('hello stdout', stdout_buffer.getvalue())
        self.assertIn('ValueError: hello stderr', stderr_buffer.getvalue())

    def test_redirect_only_stdout(self):
        stdout_buffer = io.StringIO()

        with Redirect(stdout=stdout_buffer):
            print('stdout only')

        self.assertIn('stdout only', stdout_buffer.getvalue())

    def test_redirect_only_stderr(self):
        stderr_buffer = io.StringIO()

        with Redirect(stderr=stderr_buffer):
            raise RuntimeError('stderr only')

        self.assertIn('RuntimeError: stderr only', stderr_buffer.getvalue())

    def test_streams_restored_after_exit(self):
        old_stdout = sys.stdout
        old_stderr = sys.stderr

        with Redirect():
            pass

        self.assertIs(sys.stdout, old_stdout)
        self.assertIs(sys.stderr, old_stderr)


if __name__ == '__main__':
    unittest.main()
