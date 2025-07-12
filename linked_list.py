class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        # Insert a new node at the beginning
        node = Node(data, self.head)
        self.head = node

    def output(self):
        s = ""
        itr = self.head
        if itr is None:
            print("List is empty")
            return

        while itr:
            s += str(itr.data) + "-->"
            itr = itr.next
        s = s.rstrip("-->")  # Corrected to remove the trailing '-->'
        print(s)

    def insert_end(self, data):
        # If the list is empty, create the first node
        if self.head is None:
            self.head = Node(data)
            return

        # Traverse the list to find the last node
        itr = self.head
        while itr.next:
            itr = itr.next

        # Insert the new node at the end
        itr.next = Node(data)


# Test the LinkedList operations
ll = LinkedList()
ll.insert_at_beg(5)
ll.insert_at_beg(10)
ll.output()  # Expected output: 10-->5
ll.insert_end(15)
ll.insert_end(5)
ll.output()  # Expected output: 10-->5-->15-->5
