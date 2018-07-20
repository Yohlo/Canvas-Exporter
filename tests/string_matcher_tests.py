import unittest
import json
import sys

class StringMatcherTests(unittest.TestCase):
    """
    Unit and integration testing for the StringMatcher class
    """

    def test__basic(self):
        """
        Tests basic string matching
        """
        stringSet = set(["aaa", "bbb", "ccc", "ddd", "eee", "fff"])
        stringMatcher = StringMatcher(stringSet)

        aaa = stringMatcher.match_str("aab", unique=True)
        assert aaa == "aaa"
        bbb = stringMatcher.match_str("abb", unique=True)
        assert bbb == "bbb"
        ccc = stringMatcher.match_str("ccd", unique=True)
        assert ccc == "ccc"
        ddd = stringMatcher.match_str("dde", unique=True)
        assert ddd == "ddd"
        eee = stringMatcher.match_str("eef", unique=True)
        assert eee == "eee"
        fff = stringMatcher.match_str("eee", unique=True)
        assert fff == "fff"

if __name__ == '__main__':
    sys.path.insert(0, '../')

    from string_matcher import StringMatcher

    unittest.main()