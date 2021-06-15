


class Solution(object):
    def trap(self, height):
        if len(height) < 3:
            return 0

        max_idx = 0
        cur_max = 0
        for i in range(len(height)):
            if height[i] > cur_max:
                cur_max = height[i]
                max_idx = i
        
        sum_arr = [0]
        max_left_arr = []
        max_right_arr = []
        for item in height:
            sum_arr.append(sum_arr[-1] + item)      
        
        cur_max = 0
        cur_max_index = 0
        for i, item in enumerate(height):
            if item > cur_max:
                cur_max = item
                cur_max_index = i 
            max_left_arr.append(cur_max_index)

        cur_max = 0
        cur_max_index = len(height) - 1
        
        for i, item in reversed(list(enumerate(height))):
            if item > cur_max:
                cur_max = item
                cur_max_index = i
            max_right_arr.append(cur_max_index)
        max_right_arr = list(reversed(max_right_arr))

        print(max_idx)
        print(sum_arr)
        print(max_left_arr)
        print(max_right_arr)

        total = 0

        left_index = max_idx
        while left_index != 0:
            new_left_index = max_left_arr[left_index - 1]
            total += (left_index - new_left_index - 1) * height[new_left_index] - (sum_arr[left_index] - sum_arr[new_left_index + 1])
            left_index = new_left_index


        right_index = max_idx
        while right_index != len(height) - 1:
            new_right_index = max_right_arr[right_index + 1]
            total += (new_right_index - right_index - 1) * height[new_right_index] - (sum_arr[new_right_index] - sum_arr[right_index + 1])
            right_index = new_right_index

        return total


        
        



if __name__ == "__main__":
    sol = Solution()
    a = sol.trap([0,1,0,2,1,0,1,3])
    print("result = {}".format(a))


        





        




        
    

    