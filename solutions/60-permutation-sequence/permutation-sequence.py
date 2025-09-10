import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [ix for ix in range(1, 1 + n)]

        total = 0
        while n != 0:
            curr = 0
            while k > math.factorial(n - 1):
                k = k - math.factorial(n - 1)
                curr = curr + 1
            total = 10 * total + numbers[curr]
            numbers.pop(curr)
            n = n - 1
        
        return str(total)