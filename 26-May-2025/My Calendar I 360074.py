# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.events = []

        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append((startTime, endTime))
            return True
        
        i = bisect.bisect_right(self.events, (startTime, endTime))
        

        if i > 0 and self.events[i-1][1] > startTime:
            return False
        
        if i < len(self.events) and self.events[i][0] < endTime:
            return False
        
        self.events.insert(i, (startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)