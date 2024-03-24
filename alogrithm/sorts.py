def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr, left, right):
    if left >= right:
        return 1
    i, j = left, right
    pivot = arr[left]
    while i < j:
        while i < j and arr[j] >= pivot:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        while i < j and arr[i] <= pivot:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    quick_sort(arr, left, i - 1)
    quick_sort(arr, i + 1, right)
    return arr

if __name__=="__main__":
    lists = [30,24,5,58,18,36,12,42,39]
    print("排序前的序列为：")
    for i in lists:
        print(i, end=" ")
    print("\n排序后的序列为：")
    for i in quick_sort(lists, 0, len(lists)-1):
        print(i, end=" ")
    bubble_sort(lists)
    print(lists)