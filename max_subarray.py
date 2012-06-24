def max_subarray(A):
    """
    Finds the subarray with the largest possible sum.
    Needs at least one positive value in the array.
    """
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == '__main__':
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(A))
