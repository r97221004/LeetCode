# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def titleToNumber(self, columnTitle) :
        result = 0
        
        for i, val in enumerate(columnTitle[::-1]):
            result += (ord(val) - 65 + 1)*26**i 
        
        return result
    
p = Solution()
print(p.titleToNumber("AB"))

# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def titleToNumber(self, columnTitle) :
        res = 0
        mapping = {chr(i + 64): i  for i in range(1, 27)}
        columnTitle = columnTitle[::-1]
        

        for i, val in enumerate(columnTitle):
            res += mapping[val]*(26)**i
        
        return res
    
p = Solution()
print(p.titleToNumber("AB"))