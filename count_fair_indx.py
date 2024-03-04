def build_sums_table(arr):
    """
    Build a table of cumulative sums for the given array.

    Args:
    - arr: A list representing the input array.

    Returns:
    - A list of tuples, where each tuple (s1, s2) represents the cumulative sums of two subarrays:
      s1 represents the sum of elements from arr[0] to arr[i-1],
      s2 represents the sum of elements from arr[i] to arr[N], where N is the length of arr.

    Time Complexity: O(N), where N is the length of the input array arr.

    Assumptions:
    - The length of the input array arr belongs to the range [2, 10^5].
    - Each element of the input array arr is within the range [-10^9, 10^9].
    """
    hist = [(0, sum(arr))]
    for i in range(1, len(arr)):
        prev_s1, prev_s2 = hist[i-1]
        hist.append((prev_s1+arr[i-1], prev_s2-arr[i-1]))
    return hist


def count_fair_indxs(a, b):
    """
    Count the number of fair indices between arrays a and b.

    A fair index is defined as an index that splits both arrays into two non-empty subarrays
    with equal sums.

    Args:
    - a: A list representing the first input array.
    - b: A list representing the second input array.

    Returns:
    - The number of fair indices found between arrays a and b.

    Time Complexity: O(N), where N is the length of either array a or b.

    Assumptions:
    - The length of either input array a or b belongs to the range [2, 10^5].
    - Each element of arrays a and b is within the range [-10^9, 10^9].
    """
    hist_a = build_sums_table(a)
    hist_b = build_sums_table(b)
    fair_indx_ctr = 0
    for i in range(1, len(a)):
        s1_a, s2_a = hist_a[i]
        s1_b, s2_b = hist_b[i]
        if s1_a == s2_a == s1_b == s2_b:
            fair_indx_ctr += 1
    return fair_indx_ctr


if __name__ == '__main__':
    test_cases = [
        ([0, 4, -1, 0, 3], [0, -2, 5, 0, 3]),  # should be 2
        ([2, -2, -3, 3], [0, 0, 4, -4]),  # should be 1
        ([4, -1, 0, 3], [-2, 6, 0, 4]),  # should be 0
        ([3, 2, 6], [4, 1, 6]),  # should be 0
        ([1, 4, 2, -2, 5], [7, -2, -2, 2, 5])  # should be 2
    ]

    expectation = [2, 1, 0, 0, 2]

    for idx, (a, b) in enumerate(test_cases, start=1):
        result = count_fair_indxs(a, b)
        print(f"Test case {idx}: expected {expectation[idx-1]} got {result}")


