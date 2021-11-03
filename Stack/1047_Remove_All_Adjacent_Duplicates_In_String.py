# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def removeDuplicates(self, s):
        s = list(s)
        stack = []
        
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        return ''.join(stack)

p = Solution()
print(p.removeDuplicates("abbaca"))
        