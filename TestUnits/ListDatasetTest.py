import unittest
from dataset import ListDataset


class MyTestCase(unittest.TestCase):
    dataset1 = ListDataset.ListDataset()
    dataset2 = ListDataset.ListDataset(expected_size=5, length=4)

    def test_construction(self):
        self.assertIsNotNone(self.dataset1.data)

    def test_length_1(self):
        self.assertEquals(self.dataset1.get_lenght(), 0)

    def test_length_2(self):
        self.assertEquals(self.dataset2.get_lenght(), 4)

    def test_expected_size_1(self):
        self.assertEquals(self.dataset1.get_expected_size(), 0)

    def test_expected_size_2(self):
        self.assertEquals(self.dataset2.get_expected_size(), 5)

    def test_data_size_1(self):
        datos1 = [12.32, 0.45, 4.55, 9.55]
        datos2 = [3.44, 0.67, 9.22, 0.001]
        datos3 = [3.44, 0.67, 9.22, 0.001, 4.22, 1.22]
        self.dataset1.data.append(datos1)
        self.dataset1.data.append(datos2)
        self.dataset1.data.append(datos3)

        self.assertEqual(self.dataset1.data[0], [12.32, 0.45, 4.55, 9.55])
        self.assertEqual(self.dataset1.data[0], datos1)

        self.assertEqual(self.dataset1.data[1], [3.44, 0.67, 9.22, 0.001])
        self.assertEqual(self.dataset1.data[1], datos2)

        self.assertEqual(self.dataset1.data[2], [3.44, 0.67, 9.22, 0.001, 4.22, 1.22])
        self.assertEqual(self.dataset1.data[2], datos3)

    def test_data_size_2(self):
        datos1 = [12.32, 0.45, 4.55, 9.55]
        datos2 = [3.44, 0.67, 9.22, 0.001]
        datos3 = [3.44, 0.67, 9.22, 0.001, 4.22, 1.22]
        self.dataset2.data.append(datos1)
        self.dataset2.data.append(datos2)
        self.dataset2.data.append(datos3)

        self.assertEqual(self.dataset2.data[0], [12.32, 0.45, 4.55, 9.55])
        self.assertEqual(self.dataset2.data[0], datos1)

        self.assertEqual(self.dataset2.data[1], [3.44, 0.67, 9.22, 0.001])
        self.assertEqual(self.dataset2.data[1], datos2)

        self.assertEqual(self.dataset2.data[2], [3.44, 0.67, 9.22, 0.001, 4.22, 1.22])
        self.assertEqual(self.dataset2.data[2], datos3)

    def test_labels_1(self):
        self.dataset2.labels.append(1)
        self.dataset2.labels.append(2)
        self.dataset2.labels.append(4)
        self.dataset2.labels.append(3)
        self.dataset2.labels.append(5)
        self.assertEqual(self.dataset2.get_labels(), [1, 2, 4, 3, 5])



    def test_class_map1(self):
        self.dataset1.add_series(1, [4, 3])
        self.assertEqual(self.dataset1.class_map[1], 1)
        self.assertEqual(self.dataset1.data[0], [4, 3])
        self.assertEqual(self.dataset1.labels[0], 1)

if __name__ == '__main__':
    unittest.main()