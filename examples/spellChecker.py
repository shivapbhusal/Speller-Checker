'''
A main file to check the spelling

'''
import re
import sys

def getAllWords(text):
    return re.findall(r'\w+', text.lower())

def removeExtraChars(word):
    extraCharList = ['\\','.','}','{','*','}',',','?',';','{textit}','\xe2',
                     '\x80','\x94','\x99t','\x99s','\x9d','\x9c']
    for extraChar in extraCharList:
        word = word.replace(extraChar, '')
    return word

def checkSpelling(word, wordSet):
    if word in wordSet:
        return True
    else:
        return False

wordSet = set()

with open('/usr/share/dict/words', 'r') as wordFile:
    for word in wordFile:
        word = word.strip()
        wordSet.add(word)

wordFile.close()

with open('/Users/shivabhusal/Documents/GIT/Speller-Checker/texts/wordList2.txt','r') as wordFile2:
    for word in wordFile2:
        word = word.strip()
        wordSet.add(word)

wordFile2.close()

texFile = sys.argv[1]

with open(texFile, 'r') as wordFile:
    lineNo = 1
    for line in wordFile:
        line = line.strip().split()
        for candidateWord in line:
            word = removeExtraChars(candidateWord)
            if len(word)>0:
                if not checkSpelling(word,wordSet) and not checkSpelling(word.lower(),wordSet):
                    print(lineNo,removeExtraChars(word))
        lineNo += 1


    
