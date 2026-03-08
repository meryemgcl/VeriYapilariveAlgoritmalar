# Python program for Binary Search for
# Rational Numbers without using
# floating-point arithmetic

class Rational:
    def __init__(self, num, den):
        self.p = num
        self.q = den

# Utility function to compare two
# Rational numbers 'a' and 'b'.
# It returns:
#  0 --> When 'a' and 'b' are equal
#  1 --> When 'a' is greater than 'b'
# -1 --> When 'b' is greater than 'a'
def compare(a, b):
    if a.p * b.q == a.q * b.p:
        return 0
    if a.p * b.q > a.q * b.p:
        return 1
    return -1

# Returns the index of 'x' in the list 'arr' within the range [l, r]
# if it is present, else returns -1.
# It uses Binary Search for efficient searching.
def binarySearch(arr, x):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = l + (r - l) // 2

        # If the element is present at the middle itself
        if compare(arr[mid], x) == 0:
            return mid

        # If the element is smaller than the middle element,
        # it can only be present in the left subarray
        if compare(arr[mid], x) > 0:
            r = mid - 1

        # Else, the element can only be 
        # present in the right subarray
        else:
            l = mid + 1

    # Element is not present in the array
    return -1

if __name__ == "__main__":
    arr = [Rational(1, 5), Rational(2, 3), Rational(3, 2), Rational(13, 2)]
    x = Rational(3, 2)

    print(binarySearch(arr, x))