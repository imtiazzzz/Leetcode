class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort the array in descending order
        operations = 0  # Initialize the number of operations

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                operations += i

        return operations

# Example usage:
solution = Solution()
print(solution.reductionOperations([5, 1, 3]))  # Output: 3
