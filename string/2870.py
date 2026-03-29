n = int(input())
nums = []
for _ in range(n):
    num = ''
    num_turn = False
    s = str(input())
    for c in s:
        if num_turn:
            if c.isdigit():
                num += c
            else:
                nums.append(int(num))
                num = ''
                num_turn = False
        else:
            if c.isdigit():
                num += c
                num_turn = True
    if num != '':
        nums.append(int(num))

nums.sort()
for num in nums:
    print(num)

