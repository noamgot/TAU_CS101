import unittest
import sys
from io import StringIO
import ex1, ex1sol


class Ex1TestCase(unittest.TestCase):
    pass


def generate_test(L, x, msg=None):
    def test(self):
        orig_stdout = sys.stdout
        try:
            # get test output
            new_stdout = StringIO()
            sys.stdout = new_stdout
            ex1.binary_search_print(L, x)
            test_output = new_stdout.getvalue().strip()
            # get solution output
            new_stdout = StringIO()
            sys.stdout = new_stdout
            ex1sol.binary_search_print(L, x)
            sol_output = new_stdout.getvalue().strip()
            # compare
            self.assertEqual(test_output, sol_output, msg)
        finally:
            sys.stdout = orig_stdout

    return test


test_lst = [3, 4, 5, 6, 9, 10, 13, 16, 18, 20, 22, 28, 29, 31, 32, 33, 40, 42, 47, 58, 50, 52]
nums_to_search = [18, 17]

for i in range(len(nums_to_search)):
    test_name = "test_" + str(i + 1)
    test_func = generate_test(test_lst, nums_to_search[i])
    setattr(Ex1TestCase, test_name, test_func)

if __name__ == '__main__':
    unittest.main()
