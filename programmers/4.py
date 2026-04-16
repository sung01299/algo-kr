'''
디스크 컨트롤러
Heap
'''
import heapq
def solution(jobs):
    n = len(jobs)
    answer = 0
    cur_time = 0
    heap = []
    idx = 0
    last_success = -1
    
    while idx < n:
        # enqueue
        for job in jobs:
            if last_success < job[0] <= cur_time:
                heapq.heappush(heap, (job[1], job[0]))
        
        # pop
        if heap:
            cur_job = heapq.heappop(heap)
            last_success = cur_time
            cur_time += cur_job[0]
            answer += (cur_time - cur_job[1])
            idx += 1
        else:
            cur_time += 1
        
    return answer // n