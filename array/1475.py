# 6 <-> 9
import math
from collections import defaultdict
n = str(input())

counter = defaultdict(int)

cnt = 0
for c in n:
    if int(c) == 6 or int(c) == 9:
        cnt += 1
    else:
        counter[int(c)] += 1

res1 = max(counter.values(), default=0)
res2 = math.ceil(cnt / 2)
print(max(res1, res2))
# print(max(max(counter.values()), cnt // 2))