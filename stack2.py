class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, item):
        if self.is_full():
            print("Stack Overflow: Cannot push, stack is full.")
        else:
            self.stack.append(item)
            print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: Cannot pop, stack is empty.")
            return None
        else:
            popped_item = self.stack.pop()
            print(f"Popped: {popped_item}")
            return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        else:
            top_item = self.stack[-1]
            print(f"Top element: {top_item}")
            return top_item

    def view(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            for item in reversed(self.stack):
                print(item)

def main():
    try:
        size = int(input("Enter the maximum size of the stack: "))
        my_stack = Stack(size)
    except ValueError:
        print("Invalid input. Please enter an integer for stack size.")
        return

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek (View top element)")
        print("4. View all elements")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter element to push: ")
            my_stack.push(item)
        elif choice == '2':
            my_stack.pop()
        elif choice == '3':
            my_stack.peek()
        elif choice == '4':
            my_stack.view()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()