l, c = map(int, input().split())

letters = list(map(str, input().split()))
letters.sort()

path = []

v = {'a','e','i','o','u'}

def f(start, depth):
    if depth == l:
        # check vowels, consonants
        p = ''.join(path)
        if sum(1 for ch in p if ch in v) > 0 and sum(1 for ch in p if ch not in v) >= 2:
            print(p)
        return
    
    for i in range(start, c):
        path.append(letters[i])
        f(i+1, depth+1)
        path.pop()

f(0, 0)