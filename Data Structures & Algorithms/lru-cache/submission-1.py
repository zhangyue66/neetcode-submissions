class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_list = []
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.key_list.remove(key)
            self.key_list.append(key)
            return self.cache.get(key)
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.key_list) >= self.capacity:
                cur = self.key_list.pop(0)
                del self.cache[cur]

                self.key_list.append(key)
                self.cache[key] = value
            else:
                self.key_list.append(key)
                self.cache[key] = value
        else:
            self.key_list.remove(key)
            self.key_list.append(key)
            self.cache[key] = value
            
                
