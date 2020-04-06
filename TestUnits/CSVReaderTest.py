import unittest
from core  import CSVReader

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


    def test_read_file(self):
        fileinfo = CSVReader.CSVReader.getFileInformation("/Users/morad/texto.txt", separator=" ")
        print(fileinfo)

if __name__ == '__main__':
    unittest.main()
