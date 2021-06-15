class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.currentIndex = 0

    def record(self, order_id):
        self.data[self.currentIndex] = order_id
        self.currentIndex = (self.currentIndex + 1) % self.size
       

    def get_last(self, i):
        index = (self.currentIndex - i) % self.size
        return self.data[index]

queue = CircularQueue(3)
queue.record(1)
queue.record(2)
queue.record(3)
queue.record(4)
queue.record(5)
queue.record(6)
print (queue.get_last(2))
print (queue.get_last(1))