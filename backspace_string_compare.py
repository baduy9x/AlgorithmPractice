class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []
        for item in S:
            if item == '#' and len(stack_s) != 0:
                stack_s.pop()
            elif item == '#' and len(stack_s) == 0:
                continue
            else:
                stack_s.append(item)

        for item in T:
            if item == '#' and len(stack_t) != 0:
                stack_t.pop()
            elif item == '#' and len(stack_t) == 0:
                continue
            else:
                stack_t.append(item)
        
        print("".join(stack_s))
        print("".join(stack_t))

        if "".join(stack_s) == "".join(stack_t):
            return True
        return False
        


if __name__ == "__main__":
    Solution().backspaceCompare("y#fo##f", "y#f#o##f")