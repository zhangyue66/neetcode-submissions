class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import deque
        counter = Counter(tasks)
        heap =[(-v,k) for k,v in counter.items()]
        heapq.heapify(heap)
        queue = deque()

        time = 0
        while heap or queue:
            time += 1
            if heap:
                freq,task = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    queue.append((task,freq,time+n))
            if queue:
                task,freq,next_good_time = queue[0]
                if next_good_time <= time:
                    task_name,freq,next_good_time = queue.popleft()
                    # freq += 1
                    heapq.heappush(heap,(freq,task_name))
        return time
                