class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = 0
                for x, y in directions:
                    ix = i + x
                    iy = j + y

                    if 0 <= ix < len(board) and 0 <= iy < len(board[0]):
                        if board[ix][iy] in [1, 2]: #we check 2 too because it USED to be alive, and that's what we care about (not what it will become)
                            lives += 1

                if board[i][j] == 1:
                    if lives < 2 or lives > 3:
                        board[i][j] = 2 #live -> dead
                else:
                    if lives == 3:
                        board[i][j] = 3 #dead -> live

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1