def binary_search(arr, target):
    i = 0
    j = len(arr)-1
    while i <= j:
        mid = i+(j-i)//2
        if arr[mid] > target:
            j = mid-1
        elif arr[mid] < target:
            i = mid+1
        else:
            return mid
    return i

def binary_search2(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = i+(j-i)//2
        if target < nums[mid]:
            j = j - 1
        elif target > nums[mid]:
            i = i + 1
        else:
            return mid
    return i

if __name__ == "__main__":
    arr1 = [3, 6, 8, 23, 67, 78, 99]
    f = binary_search(arr1, 67)
    print(f)
    f = binary_search(arr1, 9)
    print(f)
    f = binary_search2(arr1, 9)
    print(f)
    f = binary_search2(arr1, 100)
    print(f)
    f = binary_search2(arr1, 100)
    print(f)
