from unittest import TestCase
import app


class UnitTest(TestCase):

    def setUp(self):
        """Init"""

    def test_task5(self):
        self.assertFalse(app.word1("amsterdam"))
        self.assertTrue(app.word1("alaska"))
        self.assertTrue(app.word1("portu"))
        self.assertFalse(app.word1("rome"))

    def tearDown(self):
        """Finish"""
