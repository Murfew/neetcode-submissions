class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = -1

        cleaned = "".join(char.lower() for char in s if char.isalnum())

        for i in range(len(cleaned) // 2):
            if cleaned[left] != cleaned[right]:
                return False
            
            left += 1
            right -= 1

        return True