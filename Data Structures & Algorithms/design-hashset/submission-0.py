class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key % self.size]
        if not key in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.size]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[key % self.size]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)