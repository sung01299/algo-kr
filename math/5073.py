"""
https://www.acmicpc.net/problem/5073
"""

a, b, c = map(int, input().split())
tri_list = []
tri_list.append((a, b, c))
while a != 0 and b != 0 and c != 0:
    a, b, c = map(int, input().split())
    tri_list.append((a, b, c))

tri_list.pop()

for a, b, c in tri_list:
    if max(a, b, c) >= a + b + c - max(a, b, c):
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    elif a != b and b != c and c != a:
        print("Scalene")
    else:
        print("Invalid")