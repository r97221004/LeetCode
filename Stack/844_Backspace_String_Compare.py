# 時間複雜度: O(n + m), n = len(s) 且 m = len(t)
# 空間複雜度: O(n + m)
class Solution:
    def backspaceCompare(self, s, t):
        def build(x):
            ans = []
            for i in x:
                if i != '#':
                    ans.append(i)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        
        return build(s) == build(t)

p = Solution()
print(p.backspaceCompare("y#fo##f", "y#f#o##f"))
                