class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum() == True:
                chars.append(char.lower())
        s = "".join(chars)
        return s == s[::-1]

        