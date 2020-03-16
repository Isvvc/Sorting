def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)):
           if arr[j] < arr[smallest_index]:
               smallest_index = j

        # swap
        tmp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = tmp

    return arr


def bubble_sort( arr ):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                tmp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = tmp
                swapped = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
