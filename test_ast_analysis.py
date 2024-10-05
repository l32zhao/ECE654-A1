import unittest
from ast_analysis import analyze_code

class TestASTAnalyzer(unittest.TestCase):

    def test_identifiers_with_length_13(self):
        code = """
def some_function(): 
    pass

def identifier13char():
    pass
"""
        has_long_identifiers, _ = analyze_code(code)
        self.assertTrue(has_long_identifiers)

    def test_no_identifiers_with_length_13(self):
        code = """
def another_function():
    pass
"""
        has_long_identifiers, _ = analyze_code(code)
        self.assertFalse(has_long_identifiers)

    def test_max_nesting_level(self):
        code = """
def function_one():
    if True:
        if True:
            if True:
                if True:
                    pass
"""
        _, max_nesting_level = analyze_code(code)
        self.assertEqual(max_nesting_level, 4)

    def test_below_max_nesting_level(self):
        code = """
def function_two():
    if True:
        if True:
            if True:
                pass
"""
        _, max_nesting_level = analyze_code(code)
        self.assertEqual(max_nesting_level, 3)

if __name__ == "__main__":
    unittest.main()