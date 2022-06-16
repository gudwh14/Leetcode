class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n == 1 or s == s[::-1]:
            return s
        
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        result = ''
        for i in range(n - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result