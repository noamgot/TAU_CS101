import unittest
import ex2

test_lst = [6, 3, 12, 9, 4, 1, 5, 8]


class Ex2TestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(ex2.search_cnt(test_lst, 6), 1)

    def test_2(self):
        self.assertEqual(ex2.search_cnt(test_lst, 9), 4)

    def test_3(self):
        self.assertEqual(ex2.search_cnt(test_lst, 8), 8)

    def test_4(self):
        self.assertEqual(ex2.search_cnt(test_lst, 11), 8)


if __name__ == '__main__':
    unittest.main()
