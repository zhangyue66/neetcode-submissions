class Node:
    def __init__(self,key,val):
        self.key,self.val =key,val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # kv store

        # left point to least used. right point to most used
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next ,self.right.prev = self.right, self.left
        


    def get(self, key: int) -> int:
        if key in self.cache:
            # we need to update it to rightmost of linked list
            self.helper_remove(self.cache.get(key))
            self.helper_insert(self.cache.get(key))
            return self.cache.get(key).val
        else:
            return -1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.helper_remove(self.cache.get(key))
        self.cache[key] = Node(key,value)
        self.helper_insert(self.cache.get(key))

        if len(self.cache) > self.capacity:
            # we need to evivt the most least recently used node
            target = self.left.next
            self.helper_remove(target)
            del self.cache[target.key]



    def helper_remove(self,node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def helper_insert(self,node):
        # insert node at rightmost side
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.next = next_node
        node.prev = prev_node
        next_node.prev = node

        
