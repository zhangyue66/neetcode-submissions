class MedianFinder:

    def __init__(self):
        self.max_heap = [] # top is largest
        self.min_heap = [] # top is smallest
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) > 0 and num > self.min_heap[0]:
            heapq.heappush(self.min_heap,num)
        else:
            heapq.heappush(self.max_heap,-num)

        # rebalance
        if len(self.min_heap)-len(self.max_heap) > 1:
            cur = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-cur)

        if len(self.max_heap)-len(self.min_heap) > 1:
            cur = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,cur)
        

    def findMedian(self) -> float:
        print(self.min_heap)
        print(self.max_heap)
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        