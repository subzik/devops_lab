from unittest import TestCase
import app


class UnitTest(TestCase):

    def setUp(self):
        """Init"""

    def test_task5(self):
        self.assertFalse(app.word1("amsterdam"))
        self.assertTrue(app.word("alaska"))

    def tearDown(self):
        """Finish"""
