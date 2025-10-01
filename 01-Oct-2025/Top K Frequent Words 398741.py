# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        ans=[word for word,freq in sorted(count.items(),key=lambda x: (-x[1], x[0]))]
        return ans[:k]
        