# Find if the given number is a perfect square of an integer. This solution is through binary search

def isSqr(num):
    arr = []
    for n in range(num):
        arr.append(n)

    left = 0
    right = num

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] ** 2 == num:
            return mid
            break
        elif arr[mid] ** 2 < num:
            left = mid + 1
        else:
            right = mid - 1
    return 'No'

print(isSqr(1))