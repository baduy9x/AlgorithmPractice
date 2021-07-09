class Solution:
    def largestNumber(self, nums) -> str:
        
        check = sum([1 if x > 0 else 0 for x in nums])
        if check == 0:
            return '0'

        def compare(first, second):
            if first + second > second + first:
                return 1
            elif first + second < second + first:
                return -1
            else: return 0

        num_str = [str(x) for x in nums]

        for i in range(len(num_str) - 1):
            for j in range(i, len(num_str)):
                if compare(num_str[i], num_str[j]) == -1:
                    num_str[i], num_str[j] = num_str[j], num_str[i]
        return ''.join(num_str)

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([3,30,34,5,9]))


# class LargerNumKey(str):
#     def __lt__(x, y):
#         return x+y > y+x
        
# class Solution:
#     def largestNumber(self, nums):
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num