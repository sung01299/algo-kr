# bread
# dared
# abder -> ader, b
# adder -> ader, d
# aabbcc -> bb, aacc
# xxbbyy -> bb, xxyy

from collections import Counter

a = str(input())
b = str(input())

counter1 = Counter(a)
counter2 = Counter(b)

common = counter1 & counter2
counts = sum(common.values())

print(len(a) - counts + len(b) - counts)
