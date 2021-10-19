def bin_ser(arr, target):
    left = 0
    right = len(arr) -1

    count = 0

    while left <= right:
        '''Finding the mid below way won't cause out of bound values. mid=L+R//2 might cause out of bounds 
        values for large L and R'''
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return -1

print(bin_ser([1,2,3,4,5], -1))