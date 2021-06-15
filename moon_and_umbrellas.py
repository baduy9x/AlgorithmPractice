
def compute_cost(X, Y, input_list):
    cost = 0
    i = 0
    while input_list[i] == '?':
        i += 1
        if i == len(input_list):
            return 0
    
    prev_item = input_list[i]
    while i < len(input_list):
        i += 1

        if i == len(input_list):
            return cost

        if prev_item == 'C' and input_list[i] == 'J':
            cost += X
            prev_item = 'J'
        elif prev_item == 'J' and input_list[i] == 'C':
            cost += Y
            prev_item = 'C'
        elif input_list[i] == '?':
            while i < len(input_list) and input_list[i] == '?':
                i += 1
            if i == len(input_list):
                return cost
            if prev_item != input_list[i]:
                if prev_item == 'J':
                    cost += Y
                else:
                    cost += X
            prev_item = input_list[i]
        else:
            continue
    return cost


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        X, Y, input_list = input().split(" ")
        print("Case #{}: {}".format(i + 1, compute_cost(int(X), int(Y), input_list)))