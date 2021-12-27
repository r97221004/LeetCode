# 時間複雜度: O(n**2)
# 空間複雜度: O(n**2)
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

# 時間複雜度: O(n**2)
# 空間複雜度: O(n**2)
class Solution:
    def generate(self, numRows):
        res = [[1]*(i + 1) for i in range(numRows)]
            
        if len(res) >= 3:
            for i in range(2, len(res)):
                for j in range(1, len(res[i]) - 1):
                    res[i][j] = res[i - 1][j] + res[i - 1][j - 1]
                    
        return res
        
p = Solution()
print(p.generate(5))