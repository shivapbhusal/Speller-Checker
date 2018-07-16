'''
An example use of the package.
'''

import sys

sys.path.append(r'/Users/shivabhusal/Documents/GIT/Speller-Checker') 

import __init__ as init

testword = sys.argv[1]

print(init.checkSpelling(testword))




