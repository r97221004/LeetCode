# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def isValid(self, s):
        mapping = {'}': '{', ']': '[', ')': '('}
        stack = []

        for i in s:
            if i in mapping.values():
                stack.append(i)

            elif i in mapping.keys():
                if stack == [] or mapping[i] != stack.pop():
                    return False

        return stack == []


p = Solution()
print(p.isValid("()[]{}"))

# 時間複雜度: O(n)
# 空間複雜度: O(n)


class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True


p = Solution()
print(p.isValid("()[]{}"))
