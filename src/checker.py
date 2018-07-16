'''
A spellchecker class

'''

class Checker:
    def checkSpelling(self, word, wordDict):
        if word in wordDict:
            return True
        else:
            return False

    def autoCorrect(self, word, wordDict):
        if self.checkSpelling(word, wordDict):
            return word
        else:
            return word

