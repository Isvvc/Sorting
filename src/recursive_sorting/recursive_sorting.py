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


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
