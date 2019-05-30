import unittest

import mock

def print_hello_world():
    print hello_world()

def hello_world():
    return "Hello World"

class MockingTestTestCase(unittest.TestCase):

    @mock.patch('mock_sample.hello_world')
    def test_mock_stubs(self, test_patch):
        test_patch.return_value = 'Mocked This Silly'
        print_hello_world()
