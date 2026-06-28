class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSubarray = nums[0]
        minSubarray = nums[0]
        total = 0
        count = 0

        for i in nums:
            count += i
            count = min(i,count)

            minSubarray = min(count,minSubarray)
        
        count = 0

        for i in nums:
            if count < 0:
                count = 0
            total += i
            count += i
            
            maxSubarray = max(maxSubarray,count)
            # minSubarray = min(minSubarray,count)

        # print(maxSubarray,minSubarray)
        # print(total-minSubarray,maxSubarray)
        if maxSubarray < 0:
            return maxSubarray

        return max((total - minSubarray), maxSubarray)
