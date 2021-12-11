# 時間複雜度: O(n) 
# 空間複雜度: O(1)
class Solution:
    def romanToInt(self, s):
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        
        for i, j in zip(s, s[1:]):
            if mapping[i] >= mapping[j]:
                res += mapping[i]
            else:
                res -= mapping[i]
                
        return res + mapping[s[-1]]

p = Solution()
print(p.romanToInt("III"))
        