def findAnagrams(lstWord):
    anagrams = {}
    for word in lstWord:
        sortedWord = ''.join(sorted(word))
        if anagrams.get(sortedWord, 0) == 0:
            anagrams[sortedWord] = [word]
        else:
            anagrams[sortedWord].append(word)
    result = [group for group in anagrams.values()]
    return anagrams
