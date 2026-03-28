import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
p_sum = [0]
for i, num in enumerate(nums):
    p_sum.append(p_sum[-1] + num)

for _ in range(m):
    i, j = map(int, input().split())
    print(p_sum[j] - p_sum[i-1])