class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def add_node(self, data):
        monkey = self.root

        new_node = BTNode(data)

        while(monkey):
            if(data > monkey.data):
                if(monkey.right):
                    monkey = monkey.right
                else:
                    monkey.right = new_node
                    return self
            else:
                if(monkey.left):
                    monkey = monkey.left
                else:
                    monkey.left = new_node
                    return self
        return self

    def search_for_node(self, data):
        monkey = self.root
        while monkey:
            if data > monkey.data:
                monkey = monkey.right
            elif data < monkey.data:
                monkey = monkey.left
            elif data == monkey.data:
                return monkey.data, "I found the node!"
        return "Node Not Found"

    def min(self):
        monkey = self.root
        min = self.root.data
        while monkey.left:
            if monkey.left.data < min:
                min = monkey.left.data
            monkey = monkey.left
        return min

    def max(self):
        monkey = self.root
        max = self.root.data
        while monkey.right:
            if monkey.right.data > max:
                max = monkey.right.data
            monkey = monkey.right
        return max

    def size(self):
        if self.root == None:
            return 0
        def sizeHelp(monkey):
            if monkey is None:
                return 0
            return 1 + sizeHelp(monkey.left) + sizeHelp(monkey.right)
        return sizeHelp(self.root)

    def isEmpty(self):
        if self.root:
            return False
        return True


new_bst = BST(BTNode(10))

new_bst.add_node(7).add_node(22).add_node(11).add_node(9).add_node(4).add_node(25)

print(new_bst.search_for_node(9))
print(new_bst.search_for_node(50))

print(new_bst.min())
print(new_bst.max())
print(new_bst.size())
print(new_bst.isEmpty())


