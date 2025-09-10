class TNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        root = TNode()

        nR = len(board)
        nC = len(board[0])

        words = [word]
        for w in words:
            temp = root
            for c in w:
                temp.children[c] = TNode()
                temp = temp.children[c]
            temp.end = True

        def rec(rx, cx, node, vrec):
            if node and (0 <= rx < nR) and (0 <= cx < nC) and board[rx][cx] in node.children:
                
                c = board[rx][cx]
                node = node.children[c]

                if node.end: return True
                
                flag = False
                for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if (rx + dr, cx + dc) not in vrec:
                        vrec.add((rx + dr, cx + dc))
                        flag = flag or rec(rx + dr, cx + dc, node, vrec)
                        vrec.remove((rx + dr, cx + dc))
                
                return flag

            return False
        
        for rx in range(nR):
            for cx in range(nC):
                if rec(rx, cx, root, set([(rx, cx)])):
                    return True
        
        return False