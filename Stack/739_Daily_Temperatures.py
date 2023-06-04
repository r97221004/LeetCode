# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0]*(len(temperatures))
        stack = []  # [temp, idx]
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx

            stack.append([temp, idx])

        return res


p = Solution()
print(p.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
