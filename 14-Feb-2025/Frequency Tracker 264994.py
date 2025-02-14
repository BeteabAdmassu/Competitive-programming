# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.hashmap = defaultdict(int)  
        self.freq_map = defaultdict(int)
        

    def add(self, number: int) -> None:
        current_freq = self.hashmap[number]
        if current_freq > 0:
            self.freq_map[current_freq] -= 1  
        
        self.hashmap[number] += 1
        self.freq_map[self.hashmap[number]] += 1
    def deleteOne(self, number: int) -> None:
        if self.hashmap[number] > 0:
            current_freq = self.hashmap[number]
            self.freq_map[current_freq] -= 1 
            
            self.hashmap[number] -= 1
            if self.hashmap[number] > 0:
                self.freq_map[self.hashmap[number]] += 1  

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_map[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)