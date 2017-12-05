from django.test import TestCase

# Create your tests here.
from lotto.models import GuessNumbers


class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        t = GuessNumbers(name='apple', text='pineapple')
        t.generate()
        print(t.update_date)
        print(t.lottos)
        self.assertTrue(len(t.lottos) > 20)