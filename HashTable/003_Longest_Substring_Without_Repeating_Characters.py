# 時間複雜度: O(n)
# 空間複雜度: O(1), 因為最多存 letters, spaces, dashes
# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        output = 0
        
        for right, val in enumerate(s):
            if val not in seen:
                output = max(output, right - left + 1)
                
            else:
                if seen[val] >= left:
                    left = seen[val] + 1
                else:
                    output = max(output, right - left + 1)
            
            seen[val] = right
                
        return output
                
p = Solution()
print(p.lengthOfLongestSubstring("abcabcbb"))