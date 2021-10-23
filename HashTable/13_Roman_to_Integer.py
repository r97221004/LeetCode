# 時間複雜度: O(n) 
# 空間複雜度: O(1)
class Solution:
    def romanToInt(self, s):
        roman = {'M':1000, 'D':500, 'C': 100, 'L':50, 'X':10, 'V':5, 'I':1}
        result = 0
        
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i + 1]]:
                result += roman[s[i]]
            else:
                result -= roman[s[i]]
        
        return result + roman[s[-1]]

p = Solution()
print(p.romanToInt("III"))
        