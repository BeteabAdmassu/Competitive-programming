# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent_key = []
        self.keys = {}
        
        

    def get(self, key: int) -> int:
        if key in self.keys:
            if key in self.recent_key:
                self.recent_key.remove(key)
            self.recent_key.append(key)
            return self.keys[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.recent_key.remove(key)
        if len(self.keys) >= self.capacity and key not in self.keys:
            key_to_remove = self.recent_key.pop(0)
            del self.keys[key_to_remove]
        self.keys[key] = value
        self.recent_key.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)