# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def isValid(self, s):
        mapping = {'}':'{', ']':'[', ')':'('}
        stack = []
        
        for i in s:
            if i in mapping.values():
                stack.append(i)
            
            elif i in mapping.keys():
                if stack == [ ] or mapping[i] != stack.pop():
                    return False
                
        return stack == []

p = Solution()
print(p.isValid("()[]{}"))

# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def isValid(self, s):
        stack = []
        pair = {")": "(", "}": "{", "]": "["}
        
        for i in s:
            if not stack or i not in pair.keys(): stack.append(i)
            
            else:
                if pair[i] == stack[-1]: stack.pop()
                else: stack.append(i)
                
        return stack == []

p = Solution()
print(p.isValid("()[]{}"))