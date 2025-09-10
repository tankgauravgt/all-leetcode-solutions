class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        nR = len(board)
        nC = len(board[0])

        rowset = [set() for ix in range(9)]
        colset = [set() for ix in range(9)]
        blkset = [set() for ix in range(9)]

        def valid(board):
            for rx in range(nR):
                for cx in range(nC):
                    if board[rx][cx] in '123456789':
                        bx = 3 * (rx // 3) + (cx // 3)
                        if board[rx][cx] in rowset[rx]: return False
                        if board[rx][cx] in colset[cx]: return False
                        if board[rx][cx] in blkset[bx]: return False
                        rowset[rx].add(board[rx][cx])
                        colset[cx].add(board[rx][cx])
                        blkset[bx].add(board[rx][cx])
            return True
        
        return valid(board)