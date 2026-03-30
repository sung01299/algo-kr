from collections import Counter

vowels = {'a', 'e', 'i', 'o', 'u'}

def check_vowels(s):
    res = False
    for c in s:
        if c in vowels:
            res = True
    return res

def check_3_vowels(s):
    cnt = 0
    for c in s[:-1]:
        if c in vowels:
            cnt += 1
            if cnt >= 3:
                return False
        else:
            cnt = 0
    return True

def check_3_cons(s):
    cnt = 0
    for c in s[:-1]:
        if c not in vowels:
            cnt += 1
            if cnt >= 3:
                return False
        else:
            cnt = 0
    return True

def same_2_char(s):
    for i in range(len(s) - 2):
        if len(Counter(s[i:i+2])) == 1:
            if s[i:i+2] != 'ee' and s[i:i+2] != 'oo':
                return False
    return True

while True:
    s = str(input())
    if s == 'end':
        break

    s += '.'
    
    if not check_vowels(s) or not check_3_vowels(s) or not check_3_cons(s) or not same_2_char(s):
        print(f'<{s[:-1]}> is not acceptable.')
    else:
        print(f'<{s[:-1]}> is acceptable.')

