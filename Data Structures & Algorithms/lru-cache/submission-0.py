class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.first = None
        self.last = None
        self.map = {}

    def move_to_front(self, node: Node) -> Node:
        if node is self.first:
            return node

        prev = node.prev
        next = node.next

        # Unlink node from its current position
        if prev is None:
            # node is last
            next.prev = None
            self.last = next
        else:
            # node is in the middle
            prev.next = next
            next.prev = prev

        # Link node in at the front
        self.first.next = node
        node.prev = self.first
        node.next = None
        self.first = node

        return node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.move_to_front(node)
            return

        node = Node(value)
        node.key = key
        self.map[key] = node

        if self.first is None:
            self.last = node
        else:
            self.first.next = node
            node.prev = self.first
        self.first = node

        if len(self.map) > self.capacity:
            evict = self.last
            self.last = evict.next
            self.last.prev = None
            del self.map[evict.key]