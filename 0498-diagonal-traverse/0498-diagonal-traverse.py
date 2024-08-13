class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        i, j = 0, 0
        flow = 1  # 1 means up-right, -1 means down-left
        while len(result) < m * n:
            result.append(mat[i][j])
            if flow == 1:  # Moving up-right
                if j == n - 1:  # Hit the right border
                    i += 1
                    flow = -1
                elif i == 0:  # Hit the top border
                    j += 1
                    flow = -1
                else:  # Move diagonally up-right
                    i -= 1
                    j += 1
            else:  # Moving down-left
                if i == m - 1:  # Hit the bottom border
                    j += 1
                    flow = 1
                elif j == 0:  # Hit the left border
                    i += 1
                    flow = 1
                else:  # Move diagonally down-left
                    i += 1
                    j -= 1
        return result