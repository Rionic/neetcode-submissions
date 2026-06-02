class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validateUnit(unit):
            numUnit = []
            for num in unit:
                if num != '.':
                    numUnit.append(num)
            if len(numUnit) != len(set(numUnit)):
                return False
            return True

        for row in board:
            if not validateUnit(row):
                return False

        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not validateUnit(col):
                return False

        subgrids = []
        for i in range(3):
            subgrids.append([])
            for j in range(3):
                subgrids[i].append([])
        
        for i in range(9):
            for j in range(9):
                subgrids[i//3][j//3].append(board[i][j])
        
        for i in range(3):
            for j in range(3):
                if not validateUnit(subgrids[i][j]):
                    return False

        return True
        


                
                
            
            
