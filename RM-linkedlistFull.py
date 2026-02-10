# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     # def Printll(self):
#     #     temp = self
#     #     while temp:
#     #         print(str(temp.head))
#     #         temp = temp.next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def InsertStart(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def Printll(self):
#         temp = self.head
#         while temp:
#             print(str(temp.data))
#             temp = temp.next

#     def insertEnd(self, data):
#         new_data = Node(data)
#         temp = self.head
#         if temp is None:
#             temp = new_data
#             return

#         while temp.next:
#             temp = temp.next

#         temp.next = new_data

#     def insertbetween(self, head, end):
#         return

#     # def printllrec(self, node=None):
#     #     if node is None:  # base case
#     #         return

#     #     print(node.data, end="-->")
#     #     self.printllrec(node.next)


# # ll = Node(10)
# # ll.next = Node(20)
# # ll.next.next = Node(30)
# # ll.next.next.next = Node(50)
# # ll.Printll()
# ll = LinkedList()
# ll.InsertStart(5)
# ll.InsertStart(10)
# ll.Printll()
# ll.insertEnd(12)
# ll.Printll()
# # ll.printllrec(5)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def Insertll(self, data):
        nd = Node(data)
        nd.next = self.head
        self.head = nd

    def printll(self):
        temp = self.head
        while temp:
            print(str(temp.data), end="-->")
            temp = temp.next

    def Insertllback(self, data):
        d = Node(data)
        temp = self.head
        if temp is None:
            temp = d

        while temp.next:
            temp = temp.next
        temp.next = d

    def insertafter(self, data, n):
        nd = Node(data)
        temp = self.head

        while temp:
            if temp.data == n:
                nd.next = temp.next
                temp.next = nd
                return
            temp = temp.next

    def insertbefore(self, data, n):
        temp = self.head
        nd = Node(data)
        if not temp:
            temp = nd
            return
        if temp.data == n:
            nd.next = temp
            temp = nd
        prev = None
        while temp.next and temp.data != n:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = nd
            nd.next = temp


ll = linkedlist()
ll.Insertll(5)
ll.Insertll(10)
ll.printll()
ll.Insertllback(15)
ll.printll()
ll.insertafter(20, 5)
ll.printll()
ll.insertbefore(13, 5)
ll.printll()
