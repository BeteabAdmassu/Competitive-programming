# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        result = []

        while length > 0:
            max_index = arr.index(length)

            if max_index + 1 == length:
                length -= 1
                continue

            arr[:max_index + 1] = arr[:max_index + 1][::-1]
            arr[:length] = arr[:length][::-1]

            result.append(max_index + 1)
            result.append(length)

            length -= 1

        return result
        