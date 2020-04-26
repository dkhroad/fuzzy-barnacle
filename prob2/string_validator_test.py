import string_validator 
import unittest


class TestValidBrackets(unittest.TestCase):
    known_good_values = ( 
        ("()",True),
        ("",True),
        ("((((()))))",True),
        ("([{}()])",True),
        ("([{1}()])",True),
        ("(){}[]",True),
        ("(1234){4689}[9999]",True)
    )

    known_bad_values = (
        (" ",False),
        ("ab",False),
        (True,False),
        (12345,False),
        ("))((",False),
        ("((((())",False),
        ("([{1}(b)])",False),
    )

    def test_with_known_values(self):
        '''test with known good values'''
        for input, expected_result in self.known_good_values:
            result = string_validator.StringValidator().validate_brackets(input)
            self.assertEqual(result,expected_result)

    def test_with_bad_values(self):
        '''test with known bad values'''
        for input, expected_result in self.known_bad_values:
            result = string_validator.StringValidator().validate_brackets(input)
            self.assertEqual(result,expected_result)

if __name__ == '__main__':
    unittest.main()
