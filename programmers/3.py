'''
예상 대진표
Simulation
'''

def isMatch(a, b):
    if a < b:
        if a % 2 == 1 and a + 1 == b:
            return True
    else:
        if b % 2 == 1 and b + 1 == a:
            return True
    return False

import math
def solution(n,a,b):
    '''
    1, 2 -> 1
    3, 4 -> 2
    4 -> 2, 7 -> 4
    2 -> 1, 4 -> 2
    1 -> 1, 2 -> 1
    '''
    answer = 0
    while not isMatch(a, b):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

    return answer + 1