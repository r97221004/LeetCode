# 時間複雜度: O(n*m*4**n), n = len(word)
# 空間複雜度: O(n)
class Solution(object):
    def exist(self, board, word):
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or
                word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c))
            
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            path.remove((r, c))
            return res
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
                
        return False

p = Solution()
print(p.exist(board = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]], word = "ABCCED"))