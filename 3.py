class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:    
        # string problem, sliding window 
        result = 0
        left_pointer = 0
        seen = {}
        if not s:
            return 0
        for i, char in enumerate(s):
             # When a duplicate is seen, update the left pointer to the last time the character was seen. No need to update the left pointer one by one.
            if char in seen and left_pointer <= seen[char]:
                left_pointer = seen[char] + 1
            else:
                result = max(result, i-left_pointer + 1)
            seen[char] = i
        return result
