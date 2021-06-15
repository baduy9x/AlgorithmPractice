class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove_list = []
        stack = []
        for i, item in enumerate(s):
            if item == '(':
                stack.append(i)
            elif item == ')':
                if len(stack) == 0:
                    to_remove_list.append(i)
                else:
                    stack.pop()
            else:
                continue
        
        while len(stack) != 0:
            to_remove_list.append(stack.pop())
        
        new_s = list(s)
        for item in to_remove_list:
            new_s[item] = ""
        return "".join(new_s)

if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))