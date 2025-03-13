# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(-1)
        s = ""
        temp_char = chars[0]
        count = 0
        ptr = 0


        for i in range( len(chars)):
            if chars[i] == temp_char:
               
                count += 1
                if count > 1:
                    chars[i] = -1
                ptr = i

            else:
                if count > 1:
                    if len(str(count) )> 1:
                        for j in range(len(str(count))):
                            chars[ptr - len(str(count)) + j ] = str(count)[j]
                    else:
                        chars[ptr] = str(count)
                temp_char = chars[i]
                count = 1
                ptr = i
        print(chars)
        i = 0
        while i < len(chars):
            if chars[i] == -1:
                chars.pop(i)
            else:
                i += 1
              

    
  
            

        