import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(processed_s)
        print("".join(reversed(processed_s)))
        return processed_s == "".join(reversed(processed_s))
        

if __name__ == "__main__":
    print(Solution().isPalindrome("ab_a"))