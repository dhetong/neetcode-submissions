class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        origin_lst = [-11]*len(nums)
        queue = [origin_lst]
        for i in range(len(nums)):
            iterate_len = len(queue)
            for k in range(iterate_len):
                target_lst = queue[k]
                for j in range(len(target_lst)):
                    if target_lst[j] != -11:
                        continue
                    else:
                        tmp_lst = target_lst.copy()
                        tmp_lst[j] = nums[i]
                        queue.append(tmp_lst)
            queue = queue[iterate_len:len(queue)]
        return queue