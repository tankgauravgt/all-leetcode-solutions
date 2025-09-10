class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nR = len(board)
        nC = len(board[0])

        rowset = [set() for ix in range(9)]
        colset = [set() for ix in range(9)]
        blkset = [set() for ix in range(9)]

        for rx in range(nR):
            for cx in range(nC):
                if board[rx][cx] in '123456789':
                    bx = 3 * (rx // 3) + (cx // 3)
                    rowset[rx].add(board[rx][cx])
                    colset[cx].add(board[rx][cx])
                    blkset[bx].add(board[rx][cx])

        def rec(idx):
            if idx == nR * nC:
                return True
            rx = idx // nC
            cx = idx % nC
            bx = 3 * (rx // 3) + (cx // 3)
            if board[rx][cx] == '.':
                for n in '123456789':
                    if n not in rowset[rx] and n not in colset[cx] and n not in blkset[bx]:
                        board[rx][cx] = n
                        rowset[rx].add(n)
                        colset[cx].add(n)
                        blkset[bx].add(n)
                        if rec(1 + idx):
                            return True
                        rowset[rx].remove(n)
                        colset[cx].remove(n)
                        blkset[bx].remove(n)
                        board[rx][cx] = '.'
                return False
            else:
                return rec(1 + idx)
        
        rec(0)