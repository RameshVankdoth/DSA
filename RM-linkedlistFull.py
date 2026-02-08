class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # def Printll(self):
    #     temp = self
    #     while temp:
    #         print(str(temp.head))
    #         temp = temp.next


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def Printll(self):
        temp = self.head
        while temp:
            print(str(temp.data))
            temp = temp.next

    def insertEnd(self, data):
        new_data = Node(data)
        temp = self.head
        if temp is None:
            temp = new_data
            return

        while temp.next:
            temp = temp.next

        temp.next = new_data

    def insertbetween(self, head, end):
        return

    # def printllrec(self, node=None):
    #     if node is None:  # base case
    #         return

    #     print(node.data, end="-->")
    #     self.printllrec(node.next)


# ll = Node(10)
# ll.next = Node(20)
# ll.next.next = Node(30)
# ll.next.next.next = Node(50)
# ll.Printll()
ll = LinkedList()
ll.InsertStart(5)
ll.InsertStart(10)
ll.Printll()
ll.insertEnd(12)
ll.Printll()
# ll.printllrec(5)
