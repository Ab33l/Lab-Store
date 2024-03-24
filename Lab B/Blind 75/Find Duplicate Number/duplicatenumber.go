/*
Find the duplicate number - Find the duplicate number in an array
Input: nums = [1,3,4,2,2]
Output: 2
Input: nums = [3,1,3,4,2]
Output: 3
Input: nums = [3,3,3,3,3]
Output: 3
*/

func findDuplicate(nums []int) int {
	myDict := make(map[int]bool)
	duplicateNumber := 0
	for _, num := range nums {
		if _, exists := myDict[num]; exists {
			duplicateNumber = num
		} else {
			myDict[num] = true
		}
	}
	return duplicateNumber
}