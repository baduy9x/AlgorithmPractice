from collections import defaultdict

class Solution:
    def partitionLabels(self, s):
        last_dict = defaultdict(int)
        result = []
        for i in range(len(s)):
            last_dict[s[i]] = i
        print(last_dict)

        count = 0
        while count != len(s):
            current_item = s[count]
            last_index = last_dict[current_item]
            count += 1
            while count <= last_index:
                new_last_index = last_dict[s[count]]
                if new_last_index > last_index:
                    last_index = new_last_index
                count += 1
            result.append(last_index)
        new_result = [result[0] + 1]
        for i in range(1, len(result)):
            new_result.append(result[i] - result[i-1])


        return new_result





if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels("ababcbacadefegdehijhklij"))