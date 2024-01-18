"""
Constant time Complexity O(1)

"""

nums = [5, 6, 9, 900, 3000, 4345, 98789]


def show(list):
    if list[0] % 2 == 0:
        return 'Even'
    return 'Odd'


print(show(nums))
