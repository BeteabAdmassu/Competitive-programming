# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

       
        output = ""
        flag = False
        for word in words:
            hashmap = Counter(chars)
            for i in range(len(word)):
                if hashmap[word[i]] and hashmap[word[i]] > 0 :
                    hashmap[word[i]] -= 1
                else:
                    flag = True
                    break
    
            if flag == False:
                print(word)
                output += word
            else:
                flag = False

        return len(output)

        