class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""

        for char in s:
            if ('A' <= char <= 'Z' or
                'a' <= char <= 'z' or
                '0' <= char <= '9'):
                text += char.lower()

        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False

            left += 1
            right -= 1

        return True