class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class ll:
    def __init__(self):
        self.head = None

    def insertbeg(self, val):
        newnode = node(val, self.head)
        self.head = newnode

    def display(self):
        s = ""
        curr = self.head
        if curr is None:
            print("List is empty")
            return
        while curr:
            s += str(curr.data) + "-->"
            curr = curr.next
        print(s)

    def insertback(self, val):
        curr = self.head
        if curr is None:
            self.insertbeg(val, self.head)
        while curr.next:
            curr = curr.next

        curr.next = node(val)


ll = ll()
ll.insertbeg(5)
ll.insertbeg(10)
ll.insertbeg(15)
ll.display()
ll.insertback(30)
ll.display()
