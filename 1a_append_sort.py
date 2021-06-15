def compute_min_ops(current_item, last_item):
    if current_item > last_item:
        return current_item, 0
    len_last_item = len(str(last_item))
    len_current_item = len(str(current_item))
    new_item = current_item * (10 ** (len_last_item - len_current_item))
    if new_item > last_item:
        return new_item, (len_last_item - len_current_item)
    else:
        return new_item * 10, (len_last_item - len_current_item) + 1

def compute_min_ops_2(current_item, last_item):
    if current_item > last_item:
        return current_item, 0
    len_last_item = len(str(last_item))
    len_current_item = len(str(current_item))
    last_item_str = str(last_item)
    new_item = current_item * (10 ** (len_last_item - len_current_item))
    if new_item > last_item:
        return new_item, (len_last_item - len_current_item)
    else:
        if int(last_item_str[0:len_current_item]) > current_item:
            return new_item * 10, (len_last_item - len_current_item) + 1
        else:
            append = last_item_str[len_current_item:]
            nine_str = '9' * len(append)
            if append == nine_str:
                return new_item * 10, (len_last_item - len_current_item) + 1
            else:
                return last_item + 1, (len_last_item - len_current_item)
                  
        




        

def compute(n, input_list):
    result = 0
    for i in range(1, n):
        last_item = input_list[i - 1]
        current_item = input_list[i]
        new_item, current_ops = compute_min_ops_2(current_item, last_item)
        input_list[i] = new_item
        result += current_ops
    return result



if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n = int(input())
        input_list = [int(item) for item in input().split(" ")]
        print("Case #{}: {}".format(i + 1, compute(n, input_list)))
