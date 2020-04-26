import string_validator 
import unittest


class TestValidBrackets(unittest.TestCase):
    known_values = ( 
        ("()",True),
        (" ",False),
        ("",True),
        ("ab",False),
        ("((((()))))",True),
        ("))((",False),
        ("((((())",False),
        ("([{}()])",True),
        ("([{1}()])",True),
        ("([{1}(b)])",False),
        ("(){}[]",True),
        ("(1234){4689}[9999]",True)
    )

    def test_with_known_values(self):
        for input, expected_result in self.known_values:
            result = string_validator.validate_brackets(input)
            self.assertEqual(result,expected_result)

if __name__ == '__main__':
    unittest.main()
