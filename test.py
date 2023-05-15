# import unittest
# from io import StringIO
# from unittest.mock import patch
# from main import to_upper, say_hello


# class MyTestCase(unittest.TestCase):
#     def test_to_upper(self):
#         name = 'bhavan'
#         uupper_name = to_upper(name)
#         self.assertEqual(uupper_name, 'BHAVAN')

#     def test_say_hello(self):
#         name = 'bhavan'
#         expected_output = 'Hello, bhavan\n'

#         with patch('sys.stdout', new=StringIO()) as fake_output:
#             say_hello(name)
#             self.assertEqual(fake_output.getvalue(), expected_output)


# if __name__ == '__main__':
#     unittest.main()


import unittest
from main import to_upper


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Shubham"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "SHUBHAM")


if __name__ == '__main__':
    unittest.main()