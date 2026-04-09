from collections import defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

store = defaultdict(int)

l = 0
ans = 0
cur = 0
for r in range(len(nums)):
    if store[nums[r]] < k:
        store[nums[r]] += 1
        cur += 1
        ans = max(ans, cur)
    else:
        store[nums[r]] += 1
        cur += 1
        while store[nums[r]] > k:
            store[nums[l]] -= 1
            cur -= 1
            if store[nums[l]] == 0:
                del store[nums[l]]
            l += 1

print(ans)