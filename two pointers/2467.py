'''
-99 -98 1, 2
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

l, r = 0, n-1
ans = abs(nums[l] + nums[r])
ans_l, ans_r = l, r

while l < r:
    tmp = nums[l] + nums[r]

    if abs(tmp) < ans:
        ans_l, ans_r = l, r
        ans = abs(tmp)

        if ans == 0:
            break
    
    if tmp < 0:
        l += 1
    else:
        r -= 1

print(nums[ans_l], nums[ans_r])