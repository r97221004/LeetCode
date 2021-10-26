# 時間複雜度: O(log(n)), n = columnNumber
# 空間複雜度: O(1), 不算 resultclass Solution:
class Solution:
    def convertToTitle(self, columnNumber):
        capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # ord gets the ascii value from a character and chr vice versa.
        result = ''
        
        while columnNumber:
            columnNumber, result = (columnNumber - 1)//26, capitals[(columnNumber - 1)%26] + result  
            
        return result
    
p = Solution()
print(p.convertToTitle(28))

