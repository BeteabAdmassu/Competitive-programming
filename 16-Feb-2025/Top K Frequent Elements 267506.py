# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        sorted_hashmap_desc = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        output = []


        for i in sorted_hashmap_desc:
            if k == 0:
                break
            output.append(i)
            k -= 1
        return output



        print(sorted_hashmap_desc)
        