n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
ans = 0
l, r = 0, n-1

while l < r:
    if arr[l] + arr[r] == x:
        ans += 1
        l += 1
        r -= 1
    elif arr[l] + arr[r] < x:
        l += 1
    else:
        r -= 1

print(ans)