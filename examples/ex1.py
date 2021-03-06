'''
An example use of the package.
'''

import sys

sys.path.append(r'/Users/shivabhusal/Documents/GIT/Speller-Checker') 

import __init__ as init

testword = sys.argv[1]

print(init.checkSpelling(testword))

print(init.suggestCorrection(testword))

result = init.suggestCorrection(testword)

for word in result:
    print(word, init.getProbability(word))




