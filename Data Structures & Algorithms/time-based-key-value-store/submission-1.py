class TimeMap:

    def __init__(self):
        self.kv_store = defaultdict(list)
        self.ts_store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.kv_store[key].append(value)
        self.ts_store[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:

        if not self.kv_store.get(key):
            return ""

        timestamps = self.ts_store.get(key)
        if timestamps[0] > timestamp:
            return ""

        l,r = 0,len(timestamps)-1
        ans = ""
        while l <= r:
            mid = (l+r) //2
            if timestamps[mid] > timestamp:
                r = mid - 1
            else:
                ans = self.kv_store.get(key)[mid]
                l = mid + 1
        
        return ans
