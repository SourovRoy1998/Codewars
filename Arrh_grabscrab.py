def grabscrab(word, possible_words):
    # your code here
    from collections import Counter
    return [s for s in possible_words if Counter(s)==Counter(word)]
