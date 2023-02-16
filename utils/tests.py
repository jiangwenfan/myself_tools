import unittest

from .language import get_all_valid_words


class TestLanguage(unittest.TestCase):
    def test_get_valid_words(self):
        words = get_all_valid_words("test_res/Mini-Habits.txt")