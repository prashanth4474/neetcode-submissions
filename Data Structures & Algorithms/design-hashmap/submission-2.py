# Linked List Approach
# Uses a rudimentary hashfuntion to create buckest of items 

class LinkedListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.buckets = [LinkedListNode(0,0) for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        cur = self.getCurrentBucket(key)

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = LinkedListNode(key, value)
        # self.toList(key)
        
        

    def get(self, key: int) -> int:
        cur = self.getCurrentBucket(key)

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1

        

    def remove(self, key: int) -> None:
        cur = self.getCurrentBucket(key)

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
    
    def getCurrentBucket(self, key: int) -> int:
        return self.buckets[key % len(self.buckets)]

    def toList(self, key: int) -> List[List[int]]:
        cur = self.getCurrentBucket(key)
        items = []

        while cur.next:
            items.append([cur.next.key, cur.next.value])
            cur = cur.next
        # print( items)        
        return items
    

            



        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)