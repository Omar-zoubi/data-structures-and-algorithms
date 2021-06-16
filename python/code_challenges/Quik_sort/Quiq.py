def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)
    return arr
def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low+=1
            Swap(arr, i, low)
    Swap(arr, right, low + 1)
    return low + 1
def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp



if __name__ == "__main__":   
    print(quick_sort([7,4,10,16,6],0,4))