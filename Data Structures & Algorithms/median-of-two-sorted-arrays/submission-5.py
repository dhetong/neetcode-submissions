class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        point_1 = 0
        point_2 = 0
        n = (len(nums1) + len(nums2))//2
        count = 0
        stack = []
        while count <= n:
            if point_2 < len(nums2) and point_1 < len(nums1):
                if nums1[point_1] > nums2[point_2]:
                    stack.append(nums2[point_2])
                    point_2 += 1
                    count += 1
                else:
                    stack.append(nums1[point_1])
                    point_1 += 1
                    count += 1
            else:
                if point_2 >= len(nums2):
                    stack.append(nums1[point_1])
                    point_1 += 1
                    count += 1
                else:
                    stack.append(nums2[point_2])
                    point_2 += 1
                    count += 1
        if (len(nums1) + len(nums2)) % 2 == 1:
            return stack[len(stack)-1]
        else:
            return (stack[len(stack)-1] + stack[len(stack)-2])/2