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


def suggestCorrection(word):
    if not (checkSpelling(word)):
        return edits2(edits1(word))

def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(editedSet1):
    editedSet2 = set ()
    for word in editedSet1:
        editedSet2 = editedSet2 | edits1(word)
    return editedSet2
    

def filterDictWords(rawCandidates):
    candidateSet = set()
    for word in rawCandidates:
        if word in wordSet:
            candidateSet.add(word)
    return candidateSet
    
