class Queue:
    def __init__(self):
        # Internal list to store elements
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return "Queue -> " + str(self.items)

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")

print(q)

# Peek front elements
print("Front", q.peek()) # A


# Dequeue elements
print("Dequeue: ",q.dequeue()) # A
print("After Dequeue: ",q) # B C D


# Check the size of queue
print("Size: ",q.size()) # 3

# Check empty state
print("Is Empty?", q.is_empty())  # False

# Dequeue remaining
q.dequeue()
q.dequeue()
q.dequeue()

# Now it should be empty
print("Is Empty?", q.is_empty())  # True