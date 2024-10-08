from rich import print

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        return
    
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def display(self):
        print(f"[green]Queue: [/green]{self.queue}")

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print(f"Dequeue: {q.dequeue()}")
q.display()
print(f"Peek: {q.peek()}")
q.display()