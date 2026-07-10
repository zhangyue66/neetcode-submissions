class MedianFinder:
    # brute force
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2 != 0:
            mid = (0+len(self.nums)-1) // 2
            return self.nums[mid]
        else:
            mid = (0+len(self.nums)-1) // 2
            return (self.nums[mid]+self.nums[mid+1])/2

        