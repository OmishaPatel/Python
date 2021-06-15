from heapq import *
class MedianFinder:
    #initialize two heaps median will be on top of the maxheap
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        # insert first num into min heap
        heappush(self.min_heap, num)
        #pushing smallest num from minheap to maxheap
        heappush(self.max_heap, -heappop(self.min_heap))
        #pushing largest element which holds median value back into min heap  
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
    def findMedian(self):
        if len(self.min_heap) != len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
