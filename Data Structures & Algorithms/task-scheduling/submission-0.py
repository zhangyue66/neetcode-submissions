class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        heap = [(-v,k) for k,v in Counter(tasks).items()]
        heapq.heapify(heap)

        queue = deque([])

        time = 0 

        while queue or heap:
            time += 1
            if heap:
                freq,task_name = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    queue.append((task_name, freq, time+n)) # next available time

            if queue:
                task_name,freq,next_good_time = queue[0]
                if next_good_time<=time:
                    task_name,freq,next_good_time = queue.popleft()
                    heapq.heappush(heap,(freq,task_name))

        return time

