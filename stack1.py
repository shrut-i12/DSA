class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            return "Stack is empty!"

    def size(self):
        return len(self.items)

def run_stack_program():
    s = Stack()
    while True:
        print("\n--- Stack Operations ---")
        print("1. Push (add element)")
        print("2. Pop (remove top element)")
        print("3. Peek (view top element)")
        print("4. Check if Empty")
        print("5. Get Size")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter element to push: ")
            s.push(item)
            print(f"'{item}' pushed onto the stack.")
        elif choice == '2':
            popped_item = s.pop()
            print(f"Popped item: {popped_item}")
        elif choice == '3':
            top_item = s.peek()
            print(f"Top element: {top_item}")
        elif choice == '4':
            if s.isEmpty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif choice == '5':
            print(f"Stack size: {s.size()}")
        elif choice == '6':
            print("Exiting stack program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_stack_program()