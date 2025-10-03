#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
#by James
class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None
        

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    #insert node at right
    def insert(self, node):
        self.right.prev.next, node.prev = node, self.right.prev
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1           

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

