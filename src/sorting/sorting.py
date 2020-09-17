# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # Pointers to index of elements in arrays being merged
    a = 0
    b = 0

    # Will iterate for length of list to be merged
    for i in range(elements):
        # First two conditions allows for efficiency when one list has been merged completely
        # If A has been completely merged, merge rest of B
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        # If B has been completely merged, merge rest of A
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # If A[a] < B[b], merge A[a]
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # If B[b] < A[a], merge B[b]
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Lists must be split until len(arr) == 1
    if len(arr) > 1:
        # Slice array from beginning to midpoint
        left = merge_sort(arr[0: len(arr) // 2])
        # Slice array from midpoint to end
        right = merge_sort(arr[len(arr) // 2:])
        # Use helper function to merge with the splits as input
        arr = merge(left, right)
    
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

