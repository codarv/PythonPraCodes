
words = ['star', 'rats', 'car', 'arc', 'stars']
words2 = ['act', 'god', 'cat', 'dog', 'tac']

def anagram(words,n):
    res = []
    gIndex = []
    for x in range(n):
        if x not in gIndex:
            chkWord = words[x]
            res.append(chkWord)
            for i in range(x,n):
                if i > x:
                    if sorted(chkWord) == sorted(words[i]):
                        res.append(words[i])
                        gIndex.append(i)
            print(res)
            res.clear()

anagram(words,5)
anagram(words2,5)