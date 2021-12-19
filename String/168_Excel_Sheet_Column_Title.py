# 時間複雜度: O(log(n)), n = columnNumber
# 空間複雜度: O(1), 不算 resultclass Solution
class Solution:
    def convertToTitle(self, columnNumber):
        capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # ord gets the ascii value from a character and chr vice versa.
        result = ''
        
        while columnNumber:
            columnNumber, result = (columnNumber - 1)//26, capitals[(columnNumber - 1)%26] + result  
            
        return result
    
p = Solution()
print(p.convertToTitle(28))

# 時間複雜度: O(log(n))
# 空間複雜度: O(1)
class Solution:
    def convertToTitle(self, columnNumber):
        res = []
        m = 0
        b = columnNumber 
        
        while b:    
            b, m = divmod(b - 1, 26)
            res = [m] + res
        
        data = { i: chr(i + 65) for i in range(26)}
        res = [ data[i] for i in res]        
        return "".join(res)
    
p = Solution()
print(p.convertToTitle(28))

