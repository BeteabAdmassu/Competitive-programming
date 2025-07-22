# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_dict = {5:0, 10:0, 20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                change_dict[5] += 1
            elif bills[i] == 10 and change_dict[5] > 0:
                change_dict[5] -= 1
                change_dict[10] += 1
            elif bills[i] == 20: 
                if (change_dict[5] > 0 and change_dict[10] > 0):
                    change_dict[5] -= 1
                    change_dict[10] -= 1
                    change_dict[20] += 1
                elif (change_dict[10] == 0 and change_dict[5] >= 3):
                    change_dict[5] -= 3
                    change_dict[20] += 1
                else:
                    return False
            else:
                return False
        return True