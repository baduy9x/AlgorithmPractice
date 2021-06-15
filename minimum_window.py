from collections import Counter

class Solution:

    def check_valid(self, c1, c2):
        for item in c2:
            if (item not in c1) or c1[item] < c2[item]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        appear_ind_arr = []
        for i, item in enumerate(s):
            if item in counter_t:
                appear_ind_arr.append(i)

        if len(appear_ind_arr) == 0:
            return ""
        
        pre_counter = []
        for i in range(1, len(appear_ind_arr)):
            pre_counter.append(Counter(s[appear_ind_arr[i - 1]:appear_ind_arr[i]]))

        index = 0
        start = appear_ind_arr[index]
        counter_cur = Counter([s[start]])

        min_win = len(s) + 1
        result = ""

        while start < len(s):
            if self.check_valid(counter_cur, counter_t) and index < len(appear_ind_arr):
                current_length = start - appear_ind_arr[index] + 1
                if current_length < min_win:
                    min_win = current_length
                    result = s[appear_ind_arr[index]: (start + 1)]
                
                if index <= len(pre_counter) - 1:
                    counter_cur.subtract(pre_counter[index])
                index += 1

            else:
                start += 1
                if start == len(s):
                    break
                counter_cur.update(Counter([s[start]]))
        
        return result

        
            


if __name__ == "__main__":
    print(Solution().minWindow("aaaaaa", "a"))