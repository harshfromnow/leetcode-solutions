class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows and columns
        for k in range(9):
            l=[]
            for j in range(9):
                if '0'<= board[k][j] <='9':
                    if board[k][j] in board[k][j+1:]:
                        return False
                if '0'<= board[j][k] <='9':
                    if board[j][k] not in l:
                        l.append(board[j][k])
                    else:
                        return False
        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_seen = set()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if '0' <= board[x][y] <= '9':
                            if board[x][y] in box_seen:
                                return False
                            box_seen.add(board[x][y])
        return True