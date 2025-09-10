class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        rx = len(digits) - 1

        carry = 1
        while rx > -1:
            temp = digits[rx] + carry
            carry = temp // 10
            digits[rx] = temp % 10
            rx = rx - 1
        
        if carry:
            digits = [carry] + digits
        
        return digits