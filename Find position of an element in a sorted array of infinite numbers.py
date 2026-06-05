# Binary search function to find the element 
# in a given range
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        return binary_search(arr, mid + 1, r, x)
    return -1

# Function to find the position of the key in the 
# infinite-size array (represented as a list)
def find_pos(arr, key):
    l = 0
    h = 1

    # Find high to do binary search
    while h < len(arr) and arr[h] < key:
        # Store previous high
        l = h
        # Double high index
        h = 2 * h

    # Clamp high if it goes out of array bounds
    if h >= len(arr):
        h = len(arr) - 1

    # At this point, we have updated low and high
    # indices, thus use binary search between them
    return binary_search(arr, l, h, key)

if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    k = 170
    ans = find_pos(arr, k)
    print(ans)