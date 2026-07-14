import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ""

        for ch in s:
            if ch not in string.punctuation and ch != " ":
                result += ch

        result = result.lower()

        res = result[::-1]

        if res == result:
            return True
        else:
            return False