from collections import defaultdict

n = int(input())
options = []
for _ in range(n):
    options.append(str(input()))

'''
1. Check first letter
2. Check lowercase
'''

shortcut = set()
shortcuts = defaultdict(str)

def check_first_letter(option):
    first_letters = [0]
    for i in range(1, len(option)):
        if option[i-1] == ' ':
            first_letters.append(i)
    for i in first_letters:
        if option[i] not in shortcut and option[i].upper() not in shortcut and option[i].lower() not in shortcut:
            shortcut.add(option[i])
            shortcuts[option] = i
            return True
    return False

def check_letters(option):
    for i in range(len(option)):
        if option[i] != ' ' and option[i] not in shortcut and option[i].upper() not in shortcut and option[i].lower() not in shortcut:
            shortcut.add(option[i])
            shortcuts[option] = i
            return True
    return False

for option in options:
    assigned1 = check_first_letter(option)
    if not assigned1:
        assigned2 = check_letters(option)

def mark(option):
    res = ''
    for i in range(len(option)):
        if i == shortcuts[option]:
            res += f'[{option[i]}]'
        else:
            res += option[i]
    return res

ans = []
for option in options:
    if option in shortcuts:
        ans.append(mark(option))
    else:
        ans.append(option)

for a in ans:
    print(a)