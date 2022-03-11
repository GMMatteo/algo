class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def returnValue(self):
        if self.head is None:
            return None
        else:
            return self.head.value

    def removeFront(self, data):
        if self.head is None:
            return self.head

        cur_node = self.head

        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return self.head

    def addFront(self, data):
        new_node = SLLNode(data)
        new_node.next = self.head
        self.head = new_node

    def contains(self, data):
        cur_node = self.head

        while cur_node:
            if cur_node.data == data:
                return True

    def length(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def display(self):

        cur_node = self.head

        myList = {}

        while cur_node:
            myList.append(cur_node.data)
        return myList

    def min_nodes(self):
        
        cur_node = self.head

        min_node = cur_node.data

        while cur_node:
            if min_node > cur_node.data:
                min_node = cur_node.data
            cur_node = cur_node.next

        new_node = SLLNode(min_node)

        new_node.next = self.head
        self.head = new_node


    def max_nodes(self):

        cur_node = self.head

        max_node = cur_node.data

        while cur_node:
            if max_node < cur_node.data:
                max_node = cur_node.data
            cur_node = cur_node.next

        last_node = SLLNode(max_node)

        cur_node.next = last_node


linkedlist = SLL()