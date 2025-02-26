# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start = i + 1

        return start
        
        
        # starting_index = 0
        # for i in range(len(gas) * 2):
        #     starting_index = i
        #     tank = gas[i % len(gas)]


        #     station = i % len(gas)
        #     while tank - cost[i % len(gas)] > 0 :
        #             print( "station",station  % len(gas),"tank",tank)
                    
        #             if tank - cost[station % len(gas)] < 0:
        #                 break
        #             tank = ( tank - cost[station % len(gas)] + gas[(station +1) % len(gas)] )
                  
        #             station = (station + 1) % len(gas)
        #             print("station",station )
                 
        #             if station  == starting_index:
        #                 return station

        # return -1
    
        
               