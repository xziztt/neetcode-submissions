class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for h in range(9)]
        boxSet = [set() for b in range(9)]
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == ".":
                    continue
                boxNum = (i//3)*3 + j//3
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in boxSet[boxNum]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                boxSet[boxNum].add(board[i][j])
            
        
        return True