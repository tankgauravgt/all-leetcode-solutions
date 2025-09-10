class Solution:
    def countAndSay(self, n: int) -> str:
        
        curr = "1"
        for ix in range(n - 1):
            temp = []
            count = 1
            for cx, c in enumerate(curr):
                if cx == 0:
                    continue
                if c != curr[cx - 1]:
                    temp.append(f"{count}{curr[cx - 1]}")
                    count = 0
                count = count + 1
            temp.append(f"{count}{curr[-1]}")
            curr = "".join(temp)
        return curr