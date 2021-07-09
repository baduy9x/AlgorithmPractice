def flatten_list(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def flatten_list(mapping):
    for key in mapping:
        if isinstance(mapping[key], dict):
            value = mapping[key]


if __name__ == '__main__':
    print(flatten_list([1, 2, [3, 4, 5, [6, 7, [11, 12, [13, 14]]], 8], 9]))