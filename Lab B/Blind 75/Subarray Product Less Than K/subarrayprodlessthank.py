'''Subarray Product Less Than K
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
'''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        total_count = 0
        product = 1

        # Use two pointers to maintain a sliding window
        left = 0
        for right, num in enumerate(nums):
            product *= num  # Expand the window by including the element at the right pointer

            # Shrink the window from the left while the product is greater than or equal to k
            while product >= k:
                product //= nums[left]  # Remove the element at the left pointer from the product
                left += 1

            # Update the total count by adding the number of valid subarrays with the current window size
            total_count += right - left + 1  # right - left + 1 represents the current window size

        return total_count