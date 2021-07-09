input_arr = [7,1,5,3,6,4]

result = 0

for i in range(len(input_arr) - 1):
    max_profit = 0
    for j in range(i + 1, len(input_arr)):
        if input_arr[j] - input_arr[i] > max_profit:
            max_profit = input_arr[j] - input_arr[i]
            if max_profit > result:
                result = max_profit


print(result)

