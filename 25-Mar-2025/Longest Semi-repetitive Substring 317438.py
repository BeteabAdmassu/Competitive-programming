# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)
        left, right = 0 , 1
        prev = 0
        idx = -1
        passed = False
        long_semi = 0
        while right < len(s) and left <= right:
            if s[prev] != s[right]:
                right += 1
                prev += 1
            else:
                if passed:
                    left = idx + 1  
                passed = True
                idx = prev 
                prev = right
                right += 1
            long_semi = max(long_semi, right - left)
        return long_semi

        
        
        
        # left, right = 0 , 0
        # passed = False
        # semi = -1
        # long_semi = 0
        # unique = set()

        # while right < len(s) and left <= right:
        #     if s[right] not in unique:
        #         unique.add(s[right])
        #         right += 1
        #     else:
        #         if passed:
        #             if s[left] == semi:
        #                 semi = -1
        #                 passed = False
        #             else:
        #                 unique.remove(s[left])
        #             left += 1
        #         else:
        #             passed = True
        #             semi = s[right]
        #             right += 1
        #     long_semi = max(long_semi, right - left)
        # return long_semi

            # if s[right] != s[prev]:
            #     semi += 1
            #     prev += 1
            #     right += 1
            # else:
            #     if passed:
            #         semi = max(semi, right - left)
            #         left = idx
            #         right += 1
            #     else:
            #         passed = True
            #         prev += 1
            #         idx = right
            #         right += 1