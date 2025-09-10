from collections import deque

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        total = 0
        for c2x, c2 in enumerate(num2):
            total = 10 * total

            carry = 0
            dq = deque([])
            for c1x, c1 in enumerate(num1[::-1]):
                n1 = int(c1)
                n2 = int(c2)
                temp = n1 * n2 + carry
                carry = temp // 10
                dq.appendleft(temp % 10)
            dq.appendleft(carry)

            total = total + int(''.join(map(str, dq)))
        
        return str(total)