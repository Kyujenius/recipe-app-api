"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """calc 모듈 테스트"""
    def test_add_numbers(self):
        res = calc.add(5, 6)
        """성공"""
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = calc.sub(10, 15)
        """성공, -5가 맞다."""
        self.assertEqual(res, -5)
