import string_validator 
import unittest


class TestValidBrackets(unittest.TestCase):
    known_values = ( 
        (" ",False),
        ("ab",False)
    )

    def test_with_known_values(self):
        for input, expected_result in self.known_values:
            result = string_validator.validate_brackets(input)
            self.assertEqual(result,expected_result)

if __name__ == '__main__':
    unittest.main()
