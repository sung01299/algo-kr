while True:
    ipt = input()
    if ipt == '0':
        break
    ipts = ipt.split()
    k, nums = int(ipts[0]), ipts[1:]
    nums = [int(c) for c in nums]

    path = []
    def f(start, depth):
        if depth == 6:
            print(' '.join(map(str, path)))
            return
        
        for i in range(start, k):
            path.append(nums[i])
            f(i+1, depth+1)
            path.pop()

    f(0, 0)
    print()