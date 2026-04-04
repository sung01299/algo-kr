'''
same counter -> += 1

'''
from collections import Counter

n = int(input())
word = str(input())
word_counter = Counter(word)
words = []
for _ in range(n-1):
    words.append(str(input()))

def compare(word1, word2):
    cnt = 0
    for c in word1:
        if c in word2:
            word2[c] -= 1
            if word2[c] == 0:
                del word2[c]
        else:
            cnt += 1
    
    return sum(word2.values()), cnt

ans = 0
for w in words:
    after_compare, cnt = compare(word, Counter(w))
    if after_compare <= 1 and cnt <= 1:
        ans += 1

print(ans)