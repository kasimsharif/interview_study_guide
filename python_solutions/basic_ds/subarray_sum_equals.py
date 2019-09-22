class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        total = 0
        c_sum = {}
        c_sum[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            if c_sum.get(total - k):
                count += c_sum.get(total - k)
                
            c_sum[total] = c_sum.get(total, 0) + 1
        return countt
