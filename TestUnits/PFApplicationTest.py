import unittest
from application import PFApplication


class MyTestCase(unittest.TestCase):
    pfapplication = PFApplication.PFApplication()

    def get_app_context(self):
        self.assertEqual(True, True)

    

if __name__ == '__main__':
    unittest.main()
