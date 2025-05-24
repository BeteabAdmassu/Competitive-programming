# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

class Solution:
    def removeUtil(self, s):
        if len(s) <= 1:
            return s

        new_s = []
        i = 0
        n = len(s)

        while i < n:
            if i < n - 1 and s[i] == s[i + 1]:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                i = j
            else:
                new_s.append(s[i])
                i += 1

        new_s_str = ''.join(new_s)

        if new_s_str != s:
            return self.removeUtil(new_s_str)
        else:
            return new_s_str
