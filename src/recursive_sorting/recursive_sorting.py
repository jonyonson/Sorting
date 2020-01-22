# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    while arrA and arrB:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
        else:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
    while arrA:
        merged_arr.append(arrA[0])
        arrA.remove(arrA[0])
    while arrB:
        merged_arr.append(arrB[0])
        arrB.remove(arrB[0])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        l1 = arr[:len(arr) // 2]
        l2 = arr[len(arr) // 2:]
        # recursively call merge_sort() on LHS
        l1 = merge_sort(l1)
        # recursively call merge_sort() on RHS
        l2 = merge_sort(l2)
    # merge sorted places
    return merge(l1, l2)


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
