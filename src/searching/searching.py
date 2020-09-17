# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    '''Returns the index of the search target'''
    midpoint = (start + end) // 2
    # Empty array
    if len(arr) == 0:
        return -1
    # True condition
    if arr[midpoint] == target:
        return midpoint
    # Target is to the left of midpoint
    # Recursion, move end bounds
    elif arr[midpoint] > target:
        return binary_search(arr, target, start, midpoint - 1)
    # Target is to the right of midpoint
    # Recursion, move start bounds
    else:
        return binary_search(arr, target, midpoint + 1, end)

# # STRETCH: implement an order-agnostic binary search
# # This version of binary search should correctly find 
# # the target regardless of whether the input array is
# # sorted in ascending order or in descending order
# # You can implement this function either recursively 
# # or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

