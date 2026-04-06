import heapq, sys
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    nums = map(int, input().split())
    for num in nums:
        if len(heap) >= n:
            prev = heap[0]
            if num > prev:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        else:
            heapq.heappush(heap, num)

print(heap[0])