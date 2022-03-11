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


linkedlist = SLL()