Intuition
A naive approach would be to use two pointers starting from the beginning of both arrays and place the smaller element into nums1. However, this would overwrite elements in nums1 that have not been processed yet.

Since nums1 already contains extra space at the end, we can use that space efficiently by starting from the last valid elements of both arrays and placing the larger element at the end of nums1.

Approach
Set m and n to point to the last valid elements of nums1 and nums2 respectively.
Compare nums1[m] and nums2[n].
Place the larger element at index m + n + 1, which represents the last unfilled position in nums1.
Move the corresponding pointer backward.
Continue until one of the arrays is exhausted.
If elements remain in nums2, copy them into the remaining positions of nums1.
This ensures that all elements are merged in sorted order without using any extra space.

Complexity
Time complexity:
O(m+n)
Each element from both arrays is processed at most once.

Space complexity:
O(1)
The merge is performed in-place using the extra space already available in nums1.