class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for i in range(9)]
        colSet = [set() for i in range(9)] 
        boxSet = [set() for i in range(9)]
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == ".":
                    continue

                
                boxNum = (i//3) * 3 + j//3

                if board[i][j] in rowSet[i] or board[i][j] in colSet[j] or board[i][j] in boxSet[boxNum]:
                    return False
                
                rowSet[i].add(board[i][j])
                colSet[j].add(board[i][j])
                boxSet[boxNum].add(board[i][j])

        
        return True