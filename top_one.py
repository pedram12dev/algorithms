"""
        top one algorithm

        [1,2,1,3,4,2,5] => [1,2]

"""


def top(arr):
    values = {}
    result = []
    f_value = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
    f_value = max(values.values())
    for i in values.keys():
        if values[i] == f_value:
            result.append(i)
        else:
            continue

    return result


print(top([1, 2, 1, 3, 4, 2, 5]))
