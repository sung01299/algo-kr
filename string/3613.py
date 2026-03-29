s = str(input())

# 1: c++, 0: java
lang = 1 if '_' in s else 0

def check_java():
    if s[0].isupper():
        return False
    res = True
    for c in s:
        if not c.isalpha():
            return False
    return res

def check_c():
    alpha_turn = True
    res = True
    if s[0] == '_' or s[-1] == '_':
        return False
    for c in s:
        if alpha_turn:
            if c == '_':
                alpha_turn = False
                continue
            if not c.isalpha() or c.isupper():
                return False
        else:
            if not c.isalpha() or c.isupper():
                return False
            alpha_turn = True
    
    return res
            

def java_to_c():
    res = ''
    for c in s:
        if c.isupper():
            res += '_'
            res += c.lower()
        else:
            res += c
    return res
    
def c_to_java():
    words = s.split('_')
    res = words[0]
    for i in range(1, len(words)):
        n_word = words[i][0].capitalize()
        n_word += words[i][1:]
        res += n_word
    return res

if check_java() or check_c():
    if lang == 0:
        print(java_to_c())
    else:
        print(c_to_java())  
else:
    print('Error!')