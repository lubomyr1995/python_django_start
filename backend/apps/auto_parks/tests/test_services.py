from unittest import TestCase

from ..services import calc


class ServiceTestCase(TestCase):
    def test_plus(self):
        res = calc(2, 5, '+')
        self.assertEquals(res, 7)

    def test_minus(self):
        res = calc(5, 10, '-')
        self.assertEquals(res, -5)

    def test_multi(self):
        res = calc(3, -5, '*')
        self.assertEquals(res, -15)
