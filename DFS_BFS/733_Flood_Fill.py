# dfs  (Depth-First Search)
# 時間複雜度: O(N), N is the number of pixels in the image.
# 空間複雜度: O(N) 

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r - 1 >= 0: dfs(r - 1, c)
                if r + 1 <= R - 1 : dfs(r + 1, c)
                if c - 1 >= 0: dfs(r, c - 1)
                if c + 1 <= C -1: dfs(r, c + 1)
            
        dfs(sr, sc)
        return image
   
p = Solution()
print(p.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))