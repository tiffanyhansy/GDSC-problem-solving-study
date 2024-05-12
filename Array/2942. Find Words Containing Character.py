""" 
Link : https://leetcode.com/problems/find-words-containing-character/description/
"""

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
      new = []
      for i, word in enumerate(words):  # enumerate() to get both the index and the word from the list 
        if x in word:
          new.append(i)
        
      return new