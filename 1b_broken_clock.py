import sys
sys.stdin = open("input.txt", "r")

def compute(input_list):
    print(input_list)
    return 0

if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        input_list = [int(item) for item in input().split(" ")]
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))
        print("Case #{}: {}".format(i + 1, compute(input_list)))