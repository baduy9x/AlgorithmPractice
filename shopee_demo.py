
def get_nth_number(n):
    i = 1
    current_num_str = ['4']
    while i != n:
        last_index_of_4 = None
        for j in range(len(current_num_str) - 1, -1, -1):
            if current_num_str[j] == '4':
                last_index_of_4 = j
                break
        if last_index_of_4 is not None:
            current_num_str[last_index_of_4] = '7'
            if last_index_of_4 + 1 < len(current_num_str) and current_num_str[last_index_of_4 + 1] == '7':
                current_num_str[last_index_of_4 + 1] = '4'
        else:
            current_num_str = ['4'] * (len(current_num_str) + 1)

        i += 1
    return ''.join(current_num_str)


if __name__ == '__main__':
    for i in range(1, 100):
        print(get_nth_number(i))