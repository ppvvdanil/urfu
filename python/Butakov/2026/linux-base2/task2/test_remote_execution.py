import unittest
from unittest.mock import patch, Mock
from remote_execution import app


class TestRemoteExecution(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_timeout_error_returned(self):
        response = self.client.post('/run_code', data={
            'code': 'import time; time.sleep(2); print("done")',
            'timeout': 1,
        })

        self.assertEqual(response.status_code, 408)
        payload = response.get_json()
        self.assertIn('не уложилось', payload['error'])

    def test_invalid_form_data(self):
        response = self.client.post('/run_code', data={
            'code': 'print("ok")',
            'timeout': 31,
        })

        self.assertEqual(response.status_code, 400)
        payload = response.get_json()
        self.assertIn('timeout', payload['errors'])

    @patch('remote_execution.subprocess.Popen')
    def test_shell_false_for_unsafe_input(self, popen_mock: Mock):
        process_mock = Mock()
        process_mock.communicate.return_value = ('ok', '')
        popen_mock.return_value = process_mock

        response = self.client.post('/run_code', data={
            'code': 'print()"; echo "hacked',
            'timeout': 1,
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(popen_mock.call_args.kwargs.get('shell', True))


if __name__ == '__main__':
    unittest.main()
