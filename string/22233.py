import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = set()

for _ in range(n):
    keywords.add(str(input().rstrip()))

for _ in range(m):
    wrote = list(map(str, input().rstrip().split(',')))
    for word in wrote:
        if word in keywords:
            keywords.remove(word)
    
    print(len(keywords))