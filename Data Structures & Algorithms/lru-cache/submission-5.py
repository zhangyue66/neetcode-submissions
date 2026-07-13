class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(key=0,val=0)
        self.right = Node(key=0,val=0)
        self.left.next,self.right.prev = self.right,self.left

        self.capacity = capacity
        self.cache = {} # pointer to Linked-List node 

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache.get(key)
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key=key,val=value)
            self.insert(node)
            self.cache[key] = node
        else:
            node = self.cache.get(key)
            self.remove(node)
            node.val = value
            self.cache[key] = node
            self.insert(node)

        while len(self.cache) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]

    def remove(self,node):
        prv,nxt = node.prev,node.next
        prv.next = nxt
        nxt.prev = prv

    def insert(self,node):
        cur = self.right.prev
        self.right.prev = node
        node.next = self.right
        cur.next = node
        node.prev = cur


        
