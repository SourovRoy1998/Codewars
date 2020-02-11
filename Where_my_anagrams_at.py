def anagrams(word, words):
    #your code here
    return [s for s in words if len(s)==len(word) and set(s)==set(word)]
