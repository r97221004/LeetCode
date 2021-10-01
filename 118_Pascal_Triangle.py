# 時間複雜度: 1 + 2 + 3 + ... + n = [1 + n]*n/2 -> O(n**2)
class Solution:
    def generate(self, numRows):
        triangle = []
        
        for i in range(numRows):
            row = [0 for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row) -1):
                row[j] = triangle[i - 1][j] + triangle[i - 1][j - 1]
            
            triangle.append(row)
        
        return triangle

p = Solution()
print(p.generate(5))