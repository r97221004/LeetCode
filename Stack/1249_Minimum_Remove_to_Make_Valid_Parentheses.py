# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        s = list(s)
        
        for i, val in enumerate(s):
            if stack and val == ")" and stack[-1][1] == "(": stack.pop()       
            elif not val.isalpha(): stack.append([i, val])
                
        for i, val in stack: s[i] = ""
            
        return "".join(s)

p = Solution()
print(p.minRemoveToMakeValid("lee(t(c)o)de)"))