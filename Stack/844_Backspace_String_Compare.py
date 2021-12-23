# 時間複雜度: O(n + m), n = len(s) 且 m = len(t)
# 空間複雜度: O(n + m)
class Solution:
    def backspaceCompare(self, s, t):
        return self.helper(s) == self.helper(t)
               
    def helper(self, s):
        stack = []
        
        for i in s:
            if i != "#": stack.append(i)
            elif stack: stack.pop()
                
        return "".join(stack)

p = Solution()
print(p.backspaceCompare("y#fo##f", "y#f#o##f"))
                