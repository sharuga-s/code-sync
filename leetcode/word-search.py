class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0):
                    return True

        return False
        
    def dfs(self, board, word, i, j, count):
        if count == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "#" or board[i][j] != word[count]:
            return False

        temp = board[i][j]
        board[i][j] = "#"
        
        found = self.dfs(board, word, i + 1, j, count + 1) or self.dfs(board, word, i - 1, j, count + 1) or self.dfs(board, word, i, j + 1, count + 1) or self.dfs(board, word, i, j - 1, count + 1)

        board[i][j] = temp

        return found