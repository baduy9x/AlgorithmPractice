
def compute_cost(n, input_list):
    cost = 0
    for i in range(n-1):
        j = input_list.index(min(input_list[i:]))
        input_list[i:j + 1] = reversed(input_list[i:j + 1])
        cost += (j - i + 1)
    return cost


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n = int(input())
        input_list = [int(item) for item in input().split(" ")]
        print("Case #{}: {}".format(i + 1, compute_cost(n, input_list)))
