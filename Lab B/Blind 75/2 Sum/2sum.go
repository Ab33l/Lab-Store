/*Sample Input and Output
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].*/

func twoSum(nums []int, target int) []int {
	answerArray := make([]int, 2)
	searchElement := func(nums []int, key int) int {
		for i, element := range nums {
			if element == key {
				return i
			}
		}
		return -1
	}

	for i := 0; i < len(nums); i++ {
		target2 := nums[i]
		result := target - target2
		index := searchElement(nums, result)

		if index != -1 && index != i {
			answerArray[0] = i
			answerArray[1] = index
			sort.Ints(answerArray)
			return answerArray
		}
	}

	return answerArray
}