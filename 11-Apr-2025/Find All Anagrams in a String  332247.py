# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
  
        left, right = 0 , 0
        p_count = Counter(p)
        s_count = {}

        window_size = 0
        output = []

        while right < len(s) and left <= right:
            if window_size <= len(p):
                if s[right] in p_count:
                    if s[right] in s_count:
                        s_count[s[right]] += 1
                    else:
                        s_count[s[right]] = 1
               
            if right - left + 1 == len(p):
                if s_count == p_count:
                    output.append(left)

                if s[left] in s_count:
                    s_count[s[left]] -= 1
                    if s_count[s[left]] <= 0:
                        del s_count[s[left]]
                left += 1
            
            right += 1

        return output

            


        


     

        