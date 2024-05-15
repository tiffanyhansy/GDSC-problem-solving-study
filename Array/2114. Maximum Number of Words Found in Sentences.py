""" 
Link : https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
"""


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
      ans = 0
      for sentence in sentences:
        word = sentence.split(" ")
        count = len(word)
        ans = max(ans, count)
      
      return ans 