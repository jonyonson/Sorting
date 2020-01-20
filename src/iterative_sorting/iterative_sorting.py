# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return []

    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"

    maximum = max(arr)
    # create a count array to store the count of each unique object
    # initially the count of all elements is 0
    count = [0 for i in range(maximum + 1)]
    # count each element in the given array and place the count at the
    # appropriate index
    for x in arr:
        count[x] += 1

    a = 0
    for i in range(maximum + 1):
        for j in range(count[i]):
            arr[a] = i
            a += 1
    return arr
