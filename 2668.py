''''
1 -> 3
2 -> 1
3 -> 2

(3, 1)
''''

from collections import defaultdict

hashmap = defaultdict(int)

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

ans = []
store = set()
for i in range(n):
    if i + 1 == nums[i]:
        ans.append(nums[i])
    else:
        # if i + 1 in hashmap:
        #     if hashmap[i + 1] == nums[i]:
        #         ans.append(i + 1)
        #         ans.append(nums[i])
        # else:
        #     hashmap[nums[i]] = i + 1
        store.add()

ans.sort()
print(len(ans))
for num in ans:
    print(num)