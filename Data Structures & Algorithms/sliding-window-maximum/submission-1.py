class SegmentTree:
    def __init__(self, N, A):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.build(N, A)
    def build(self, N, A):
        self.tree = [float('-inf')] * (2 * self.n)
        for i in range(N):
            self.tree[self.n + i] = A[i]
        for i in range(self.n-1,0,-1):
            self.tree[i] = max(self.tree[i<<1], self.tree[i<<1|1])
    def search(self, l, r):
        res = float('-inf')
        l = l + self.n
        r = r + self.n
        while l < r:
            if l & 1:
                res = max(self.tree[l], res)
                l += 1
            if r & 1:
                r -= 1
                res = max(self.tree[r], res)
            l >>= 1
            r >>= 1
        return res
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seg_tree = SegmentTree(len(nums), nums)
        output = []
        for i in range(len(nums)-k+1):
            output.append(seg_tree.search(i, i+k))
        return output
        