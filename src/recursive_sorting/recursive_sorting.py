def merge( arrA, arrB ):
    merged_arr = []

    done = False
    while len(arrA) + len(arrB) > 0:
        if len(arrA) == 0:
            merged_arr += arrB
            arrB = []
        elif len(arrB) == 0:
            merged_arr += arrA
            arrA = []
        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    
    return merged_arr


import math
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        return merge([arr[0]],[arr[1]])
    elif len(arr) == 3:
        arrA = [arr[2]]
        arrB = merge([arr[0]],[arr[1]])
        return merge(arrA, arrB)
    else:
        arrA = arr[:int(math.ceil(len(arr) / 2))]
        arrB = arr[-1 * int(math.floor(len(arr) / 2)):]
        arrA_sorted = merge_sort(arrA)
        arrB_sorted = merge_sort(arrB)
        return merge(arrA_sorted, arrB_sorted)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
