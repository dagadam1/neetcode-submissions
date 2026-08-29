class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key % self.size]
        #if key not in [k for (k, v) in bucket]:
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[key % self.size]
        for (k, v) in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.size]
        for (k, v) in bucket:
            if k == key:
                bucket.remove((k, v))



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)