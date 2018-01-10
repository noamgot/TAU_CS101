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
            ex1.search_print(L, x)
            test_output = new_stdout.getvalue().strip()
            # get solution output
            new_stdout = StringIO()
            sys.stdout = new_stdout
            ex1sol.search_print(L, x)
            sol_output = new_stdout.getvalue().strip()
            # compare
            self.assertEqual(test_output, sol_output, msg)
        finally:
            sys.stdout = orig_stdout

    return test


test_lst = [4, 7, 2, 3, 1]
nums_to_search = [7, 8]

for i in range(len(nums_to_search)):
    test_name = "test_" + str(i + 1)
    test_func = generate_test(test_lst, nums_to_search[i])
    setattr(Ex1TestCase, test_name, test_func)

if __name__ == '__main__':
    unittest.main()
