class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.freq = []
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.freq.remove(key)
            self.freq.append(key)
            return self.cache.get(key)
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.freq.append(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.freq.remove(key)
            self.freq.append(key)

        while len(self.freq) > self.capacity:
            cur = self.freq.pop(0)
            del self.cache[cur]