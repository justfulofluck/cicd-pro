import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = 'bhavan'
        uupper_name = to_upper(name)
        self.assertEqual(uupper_name, 'bhavan')

if __name__ == '__main__':
    unittest.main()
    