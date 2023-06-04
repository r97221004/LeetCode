# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def carFleet(self, target: int, position, speed):
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


p = Solution()
print(p.carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))
