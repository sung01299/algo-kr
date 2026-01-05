"""
https://www.acmicpc.net/problem/23971
"""

import math

row, col, n, m = map(int, input().split(' '))

a = math.ceil(row / (n + 1)) * math.ceil(col / (m + 1))

print(a)