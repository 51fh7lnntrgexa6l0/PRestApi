
from django.test import TestCase
from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Testing Add Numbers.
            Two numbers are added together.
        """
        self.assertEqual(add(3,8),11)
