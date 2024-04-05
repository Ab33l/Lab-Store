/*Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
*/

func singleNumber(nums []int) int {
	appearance := make(map[int]int)
	for _, num := range nums {
		appearance[num] += 1
	}
	for num, val := range appearance {
		if val == 1 {
			return num
		}
	}
	return 0
}