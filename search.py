def binary_search(arr, target):
    n = len(arr)
    i = 0
    j = n-1
    while i <= j:
        if arr[i+(j-i)//2] > target:
            j = i+(j-i)//2
            i = i+1
        elif arr[i+(j-i)//2] < target:
            i = i+(j-i)//2
            j = j-1
        else:
            return i+(j-i)//2
    return -1


if __name__ == "__main__":
    arr1 = [3, 6, 8, 23, 67, 78, 99]
    f = binary_search(arr1, 67)
    print(f)
    f = binary_search(arr1, 9)
    print(f)