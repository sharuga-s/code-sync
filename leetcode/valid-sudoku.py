class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # rows

        for i in board:
            if not self.isValid(i):
                return False
        
        # cols

        for i in range(9):
            coli = []
            
            for j in board:
                coli.append(j[i])
            
            if not self.isValid(coli):
                return False
        
        # boxes

        for i in range(0, 9, 3):
            box1 = board[i][:3] + board[i + 1][:3] + board[i + 2][:3]
            box2 = board[i][3:6] + board[i + 1][3:6] + board[i + 2][3:6]
            box3 = board[i][6:] + board[i + 1][6:] + board[i + 2][6:]

            print(box1)
            print(self.isValid(box1))

            if not self.isValid(box1) or not self.isValid(box2) or not self.isValid(box3):
                return False
    
        return True
    
    def isValid(self, arr):
        seen = []
        for i in arr:
            if i == '.':
                continue

            if (i < '1' or i > '9'):
                return False
            
            if i in seen:
                return False
                
            seen.append(i)
            
        
        return True