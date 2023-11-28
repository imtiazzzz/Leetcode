class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        # Calculate the sum of absolute differences for the right side of each element
        right_sum = [0] * n
        right_sum[n-1] = 0
        for i in range(n-2, -1, -1):
            right_sum[i] = right_sum[i+1] + (nums[i+1] - nums[i]) * (n - i - 1)
        
        # Calculate the sum of absolute differences for the left side of each element
        left_sum = 0
        result = []
        for i in range(n):
            result.append(left_sum + right_sum[i])
            if i < n - 1:
                left_sum += (nums[i+1] - nums[i]) * (i + 1)
        
        return result

# Example usage:
solution = Solution()
print(solution.getSumAbsoluteDifferences([2,3,5]))  # Output: [4,3,5]
print(solution.getSumAbsoluteDifferences([1,4,6,8,10]))  # Output: [24,15,13,15,21]
