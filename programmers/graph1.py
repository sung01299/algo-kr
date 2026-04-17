'''
타겟 넘버
DFS
'''

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def backtracking(cur, idx):
        nonlocal answer
        if idx == n:
            if cur == target:
                answer += 1
            return
        
        backtracking(cur + numbers[idx], idx + 1)
        backtracking(cur - numbers[idx], idx + 1)
    
    backtracking(0, 0)
    print(answer)
    return answer