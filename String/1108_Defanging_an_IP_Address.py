# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def defangIPaddr(self, address):
        return '[.]'.join(address.split('.'))

p = Solution()
print(p.defangIPaddr("1.1.1.1"))        


# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')

p = Solution()
print(p.defangIPaddr("1.1.1.1"))        