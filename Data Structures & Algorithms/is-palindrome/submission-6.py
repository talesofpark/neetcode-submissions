class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = []
        for word in s[::-1]:
            if word.isalnum():
                reverse.append(word.lower())
        normal = []
        for word in s: 
            if word.isalnum():
                normal.append(word.lower())
        
        return normal == reverse
