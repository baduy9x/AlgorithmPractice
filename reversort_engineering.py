import itertools

def compute_cost(n, input_list):
    cost = 0
    for i in range(n-1):
        j = input_list.index(min(input_list[i:]))
        input_list[i:j + 1] = reversed(input_list[i:j + 1])
        cost += (j - i + 1)
    return cost

def gen_list(n, cost):
    ans = [i for i in range(n)]
    permu = list(itertools.permutations(ans))
    for item in permu:
        if compute_cost(n, list(item)) == cost:
            return [x + 1 for x in item]
    return None

if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n, cost = [int(item) for item in input().split(" ")]
        ans = gen_list(n, cost)
        if ans is None:
            print("Case #{}: IMPOSSIBLE".format(i + 1))
        else:
            output = " ".join([str(x) for x in ans])
            print("Case #{}: {}".format(i + 1, output))
