/*Majority Element
Given an array nums of size n, return the majority element.
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
*/

func majorityElement(nums []int) int {
	appearance := make(map[int]int)
	var checker int = 0
	var finalNum int = 0
	for _, num := range nums {
		appearance[num] += 1
	}

	for num, val := range appearance {
		if val > checker {
			checker = val
			finalNum = num
		}
	}
	return finalNum
}