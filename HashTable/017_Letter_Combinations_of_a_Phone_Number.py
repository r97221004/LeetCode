# 時間複雜度: ?
# 空間複雜度: ?
class Solution(object):
    def letterCombinations(self, digits):
        data = {'2': "abc", 
                '3': "def", 
                '4': "ghi", 
                '5': "jkl", 
                '6': "mno", 
                '7': "pqrs", 
                '8': "tuv", 
                '9': "wxyz"}
        
        cmb = [''] if digits else []
        
        for d in digits:
            cmb = [p + q for p in cmb for q in data[d]]
            
        return cmb

p = Solution()
print(p.letterCombinations("23"))