class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Forward traversal:", " <-> ".join(elements))

    def display_backward(self):
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("Backward traversal:", " <-> ".join(elements))

# Taking input from the user
dll = DoublyLinkedList()
while True:
    user_input = input("Enter an element to add to the list (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        data = int(user_input) # Assuming integer input for simplicity
        dll.append(data)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Displaying the list
dll.display_forward()
dll.display_backward()