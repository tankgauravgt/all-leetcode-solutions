class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def rec(w1, w2):
            if w1 == len(word1) and w2 == len(word2):
                return 0
            
            if w1 == len(word1):
                return len(word2) - w2
            
            if w2 == len(word2):
                return len(word1) - w1
            
            matched = word1[w1] == word2[w2]
            if matched:
                return rec(1 + w1, 1 + w2)
            else:
                temp1 = 1 + rec(1 + w1, w2)
                temp2 = 1 + rec(w1, 1 + w2)
                temp3 = 1 + rec(1 + w1, 1 + w2)
                return min(temp1, temp2, temp3)
        
        return rec(0, 0)