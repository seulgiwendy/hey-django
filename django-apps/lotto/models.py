from __future__ import unicode_literals

from random import random

from django.db import models

# Create your models here.
from django.utils import timezone


class GuessNumbers(models.Model):
    name = models.CharField(max_length = 24)
    lottos = models.CharField(max_length = 255, default = '[1,2,3,4,5,6]')
    text = models.CharField(max_length=100, default="fuck you!")
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ""
        origin = list(range(1,46))
        for i in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + "\n"
        self.update_date = timezone.now()
        self.save()




