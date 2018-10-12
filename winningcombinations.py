#!/usr/bin/python
# Created by Edmhar Laoag 

import sys
import random

class lottery(object):
    @staticmethod
    def sixFiftyEight():
        ultraMega = set()
        while len(ultraMega) < 6:
            ultraMega.add(random.randint(1,58))
        generateNumbers = list(ultraMega)
        return generateNumbers

winningCombinations = lottery()
counter = range(int(sys.argv[1]))
for count in counter:
    print("Possible winning combination for Ultra Mega Draw: ", lottery.sixFiftyEight())

