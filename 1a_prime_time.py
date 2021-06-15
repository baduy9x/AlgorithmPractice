def get_bins(n, bs = ''):
    result = []
    def genbin(n, bs = ''):
        if n-1:
            genbin(n-1, bs + '0')
            genbin(n-1, bs + '1')
        else:
            result.append('1' + bs)
    genbin(n)
    return result

def compute(input_list):
    result = 0
    all_bin = get_bins(len(input_list))
    print(len(all_bin))
    for item in all_bin:
        tong_arr = []
        for i, j in enumerate(item):
            if j == '0':
                tong_arr.append(input_list[i])
        tong = sum(tong_arr)
        tich_arr = []
        for i, j in enumerate(item):
            if j == '1':
                tich_arr.append(input_list[i])
        tich = 1
        for i in tich_arr:
            tich = tich * i
        if tong == tich and tong > result:
            result = tong
    return result

if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        m = int(input())
        input_list = []
        for i in range(m):
            p, freq = [int(x) for x in input().split(" ")]
            for i in range(freq):
                input_list.append(p)
        print("Case #{}: {}".format(i + 1, compute(input_list)))
