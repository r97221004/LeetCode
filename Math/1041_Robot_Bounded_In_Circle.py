# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def isRobotBounded(self, instructions):
        x = y = 0
        direction = 0
        moves = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}

        for instruction in instructions:
            if instruction == "L":
                direction = (direction + 3)%4
            elif instruction == "R":
                direction = (direction + 1)%4
        
            else:
                x += moves[direction][0]
                y += moves[direction][1]
        
        return (x == 0 and y ==0) or direction != 0

p = Solution()
print(p.isRobotBounded("GGLLGG"))