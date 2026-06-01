"""
Using Linked List
"""

class LinkedListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.buckets = [LinkedListNode(0) for _ in range(10000)]
        
    def add(self, key: int) -> None:
        current_bucket_items = self.buckets[self.hash(key)]
        while current_bucket_items.next:
            if current_bucket_items.next.key == key:
                return
            current_bucket_items = current_bucket_items.next
        current_bucket_items.next = LinkedListNode(key)

        

    def remove(self, key: int) -> None:
        current_bucket_items = self.buckets[self.hash(key)]
        while current_bucket_items.next:
            if current_bucket_items.next.key == key:
                current_bucket_items.next = current_bucket_items.next.next
                return
            current_bucket_items = current_bucket_items.next
        

        

    def contains(self, key: int) -> bool:
        current_bucket_items = self.buckets[self.hash(key)]
        while current_bucket_items.next:
            if current_bucket_items.next.key == key:
                return True
            current_bucket_items = current_bucket_items.next
        return False

    def hash(self, key: int) -> int:
        return key % len(self.buckets)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)