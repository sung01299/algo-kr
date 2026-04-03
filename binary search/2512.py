'''
1st approach: binary search
'''
import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
total = int(input())

def calculate(limit):
    ans = 0
    for budget in budgets:
        ans += min(budget, limit)
    return ans

def binary_search():
    l, r = 0, max(budgets)
    while l < r:
        mid = l + (r - l) // 2
        if calculate(mid) > total:
            r = mid
        else:
            l = mid + 1
    return l - 1

if sum(budgets) <= total:
    print(max(budgets))
else:
    print(binary_search())