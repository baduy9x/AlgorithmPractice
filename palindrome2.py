class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     if s == "".join(reversed(s)):
    #         return True
        
    #     for i in range(len(s)):
    #         new_s = s[:i] + s[(i + 1):]
    #         if new_s == "".join(reversed(new_s)):
    #             return True
    #     return False

    def validPalindrome(self, s: str) -> bool:
        if s == "".join(reversed(s)):
            return True
        return self.valid(s, True) or self.valid(s, False)

    def valid(self, s: str, is_left: bool) -> bool:
        left = 0
        right = len(s) - 1
        used = False
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right] and used == False:
                used = True
                if is_left:
                    left += 1
                else: right -= 1
            else:
                break
        return left > right
        


        





if __name__ == "__main__":
    print(Solution().valid("abcdba", True))
            