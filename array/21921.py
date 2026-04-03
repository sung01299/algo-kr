import sys
from collections import defaultdict
input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]
for i in range(len(nums)):
    prefix.append(nums[i] + prefix[-1])

max_visitor = 0
visitors = defaultdict(int)
for i in range(len(nums) - x + 1):
    max_visitor = max(max_visitor, prefix[i+x] - prefix[i])
    visitors[prefix[i+x] - prefix[i]] += 1

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(visitors[max_visitor])