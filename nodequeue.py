
class Node:
    def __init__(self, data):
        self.data = data  # Holds the data
        self.next = None  # Reference to the next node

class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    def enqueue(self, data):
        new_node = Node(data)
        
        # If the queue is empty, both front and rear point to the new node
        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        # Add the new node at the end of the queue and update the rear
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        # If the queue is empty, return None
        if self.front is None:
            print("Queue is empty!")
            return None
        
        # Get the data from the front node and move the front pointer to the next node
        temp = self.front
        self.front = self.front.next
        
        # If the queue becomes empty after dequeue, set rear to None
        if self.front is None:
            self.rear = None
        
        return temp.data

    def peek(self):
        if self.front is None:
            print("Queue is empty!")
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None

    def display(self):
        if self.front is None:
            print("Queue is empty!")
            return
        
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue after enqueueing 10, 20, 30:")
q.display()

print("Front of the queue:", q.peek())

print("\nDequeued:", q.dequeue())
q.display()

print("\nDequeued:", q.dequeue())
q.display()

print("\nIs the queue empty?", q.is_empty())

print("\nDequeued:", q.dequeue())
q.display()

print("\nIs the queue empty?", q.is_empty())
