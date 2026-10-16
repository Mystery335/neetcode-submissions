class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        s = s.lower()
        for char in s:
            if char.isalpha() == True or char.isdigit() == True:
                new_str += char
        return new_str == new_str[::-1]
        