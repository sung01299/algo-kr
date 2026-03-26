"""
10^11 mod 12

Base Case:
k == 1: a mod c

induction:

"""

a, b, c = map(int, input().split())

def power(a, b, c):
    if b == 1:
        return a % c
    val = power(a, b//2, c)
    if b % 2 == 0:
        return (val * val) % c
    else:
        return (val * val * a) % c

print(power(a, b, c))