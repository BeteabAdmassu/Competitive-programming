# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = { "".join(sorted(i)):[] for i in strs}
        final = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in hashmap:
                hashmap[sortedWord].append(word)
        for i in hashmap:
            final.append(hashmap[i])
        return final

        
    

        
