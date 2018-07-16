'''
A main file to check the spelling

'''
wordSet = set()

with open('wordList.txt', 'r') as wordFile:
    for word in wordFile:
        word = word.strip()
        wordSet.add(word)

wordFile.close()

def checkSpelling(word):
    if word in wordSet:
        return True
    else:
        return False
    
