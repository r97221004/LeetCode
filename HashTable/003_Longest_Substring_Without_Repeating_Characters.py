# 時間複雜度: O(n)
# 空間複雜度: O(1), 因為最多存 letters, spaces, dashes
# Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):
        data = {}
        longest = 0
        start = 0
        for i, val in enumerate(s):
            if val not in data:
                data[val] = i
            
            # 考慮 "abba"
            elif data[val] < start:
                data[val] = i
                
            else:
                longest = max(longest, i - start)
                start = data[val] + 1
                data[val] = i
                
        return max(longest, len(s) - start)
                
p = Solution()
print(p.lengthOfLongestSubstring("abcabcbb"))