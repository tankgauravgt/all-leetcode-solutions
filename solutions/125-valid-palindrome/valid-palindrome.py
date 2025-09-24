class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = list(filter(str.isalnum, s))
        return temp == temp[::-1]