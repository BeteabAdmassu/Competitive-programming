# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        left = 0 
        right = 0 
        output = []
        while left < len(firstList) and right < len(secondList):
            start = max(firstList[left][0], secondList[right][0])
            end = min(firstList[left][1], secondList[right][1])

            if start <= end:
                output.append([start, end])
            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1

        return output



        