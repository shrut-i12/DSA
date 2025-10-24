class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  

    
    def append(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
        else:
            last = self.head
            while last.next:  
                last = last.next
            last.next = new_node  

    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    
    def delete_node(self, key):
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  
            print("Node not found")
            return

        prev.next = current.next
        current = None 


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    print("Linked List:")
    ll.print_list()  

    ll.delete_node(20)
    print("After deleting 20:")
    ll.print_list()  