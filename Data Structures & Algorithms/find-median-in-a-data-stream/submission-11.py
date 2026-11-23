class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        

    def addNum(self, num: int) -> None:
        if not self.lower:
            heapq.heappush(self.lower, -num)
            return
        if num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)
        if len(self.lower) - len(self.upper) >= 2:
            largest = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, largest)
        elif len(self.upper) - len(self.lower) >= 1:
            smallest = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -smallest)


    def findMedian(self) -> float:
        # print(self.upper)
        # print(self.lower)
        if len(self.upper) == len(self.lower):
            return (self.upper[0] + -self.lower[0]) / 2
        return -self.lower[0]
        
        