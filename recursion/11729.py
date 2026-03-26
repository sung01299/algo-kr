"""
f(2): 1번원판이 2 -> 1번 원판 2로 -> 2번 원판 3으로 -> 1번 원판 3으로
f(3): 1-2번 원판이 2 -> 3번 원판 3으로 -> 1-2번 3으로

f(k): 1-(k-1)번 원판이 2 -> k번 원판 3으로 -> 1-(k-1)번 원판 3으로
"""

n = int(input())

path = []

def hanoi(n, start, end):
    if n == 1:
        path.append((start, end))
        print(start, end)
        return
    
    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

print(2**n - 1)
hanoi(n, 1, 3)