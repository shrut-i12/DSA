class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        self.items.append(item)
        print(f"'{item}' enqueued.")

    def dequeue(self):
        """Removes and returns the item from the front of the queue."""
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"'{item}' dequeued.")
            return item
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def view(self):
        """Displays the current elements in the queue."""
        if not self.is_empty():
            print("Current queue elements:", self.items)
        else:
            print("Queue is empty.")

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

def main():
    q = Queue()

    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue (Push)")
        print("2. Dequeue (Pop)")
        print("3. View Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.view()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()