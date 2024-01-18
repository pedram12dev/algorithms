"""
Logarithm Time O(log n)

"""

nums = [0,4,7,10,14,23,45,47,53]


def show(list , element):
    for i in list:
        if i == element:
            return list.index(i)


print(show(nums , 47))