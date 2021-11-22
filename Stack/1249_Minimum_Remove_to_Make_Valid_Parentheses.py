# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stack = []
        
        for i, val in enumerate(s):
            if val == "(":
                stack.append(i)
            elif val == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        
        while stack:
            s[stack.pop()] = ""
            
        
        return  "".join(s)

p = Solution()
print(p.minRemoveToMakeValid("lee(t(c)o)de)"))