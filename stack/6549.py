"""
최대 넓이: 이전 직사각형 포함 넓이
2, 1, 1, 1, 1, 1, 1

"""
import sys
input = sys.stdin.readline

while True:
    case = list(map(int, input().split()))
    if case[0] == 0: break
    N, heights = case[0], case[1:case[0] + 1]
    rev_heights = list(reversed(heights))
    # if detect any smaller new elem, calculate, empty stack and restart
    fromL, fromR = max(heights), max(heights)
    stack = []
    for idx in range(N):
        if stack and heights[idx] < stack[-1]:
            fromL = max(fromL, min(heights[idx], min(stack)) * (len(stack) + 1))
            stack = []
        else:
            stack.append(heights[idx])
        fromL = max(fromL, min(stack, default=0) * len(stack))

    stack = []
    for idx in range(N):
        if stack and rev_heights[idx] < stack[-1]:
            fromR = max(fromR, min(rev_heights[idx], min(stack)) * (len(stack) + 1))
            stack = []
        else:
            stack.append(rev_heights[idx])
        fromR = max(fromR, min(stack, default=0) * len(stack))

    print(max(fromL, fromR))