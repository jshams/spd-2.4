class LinkedList():
    def __init__(self, items=[]):
        self.size = 0
        self.head = None
        self.tail = None
        self.create(items)

    def create(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        node = LinkedNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def get_items(self):
        node = self.head
        items = []
        for _ in range(self.size):
            items.append(node.data)
            node = node.next
        return items


class LinkedNode():
    def __init__(self, data):
        self.data = data
        self.next = None
