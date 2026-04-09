s = str(input())
t = str(input())

a_count = t.count('A')
b_count = t.count('B')

ans = False

def backtracking(cur, target):
    if len(cur) == len(target):
        return cur == target
    
    if cur[-1] == 'A':
        if backtracking(cur[:-1], s):
            return True
    if cur[0] == 'B':
        if backtracking(cur[1:][::-1], s):
            return True
    
    return False

print(int(backtracking(t, s)))
    
