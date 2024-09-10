class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


solution = Solution()

nums1 = [1, 3]
nums2 = [2, 4]

r = solution.findMedianSortedArrays(nums1, nums2)

print(r)


nums1 = [56, 89]
nums2 = [34, 67]

r = solution.findMedianSortedArrays(nums1, nums2)

print(r)

nums1 = [12, 45]
nums2 = [23, 78]

r = solution.findMedianSortedArrays(nums1, nums2)

print(r)

nums1 = [67, 91]
nums2 = [4, 36]

r = solution.findMedianSortedArrays(nums1, nums2)

print(r)

nums1 = [18, 54]
nums2 = [29, 82]

r = solution.findMedianSortedArrays(nums1, nums2)

print(r)
