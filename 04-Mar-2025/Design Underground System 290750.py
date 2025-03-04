# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkin = defaultdict()
        self.stations = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin = self.checkin[id]
        if (checkin[0],stationName) in self.stations:
            self.stations[(checkin[0],stationName)][0] +=  t-checkin[1]
            self.stations[(checkin[0],stationName)][1] +=  1
        else:
            self.stations[(checkin[0],stationName)] = [0,0]
            self.stations[(checkin[0],stationName)][0] =  t-checkin[1]
            self.stations[(checkin[0],stationName)][1] =  1  

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stations[(startStation,endStation)][0] / self.stations[(startStation,endStation)][1]


        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)