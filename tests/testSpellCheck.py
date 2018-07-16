'''
Unit test for SpellChecker
'''

import sys

sys.path.append(r'/Users/shivabhusal/Documents/GIT/Speller-Checker/')

import unittest

import __init__ as init

class TestMethods(unittest.TestCase):
    def testVerb(self):
        self.assertEqual(init.checkSpelling('writing'),True)
        self.assertEqual(init.checkSpelling('writin'),False)

if __name__ == '__main__':
    unittest.main()
