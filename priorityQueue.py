import heapq as hq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        hq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return hq.heappop(self.queue)[-1]

    def is_empty(self):
        return len(self.queue) == 0


pq = PriorityQueue()
print("Max Priority Queue: ")
pq.push("task1", priority=6)
pq.push("task2", priority=5)
pq.push("task3", priority=10)

while pq.is_empty()!=True:
    print(pq.pop())