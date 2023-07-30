class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        dequeued_item = self.queue[0]
        self.queue = self.queue[1:]
        return dequeued_item

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]
