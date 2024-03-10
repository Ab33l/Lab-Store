/*
Intersection of two arrays - find unique elements in two arrays in any order and should be unique numbers in final array output
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
*/
func intersection(nums1 []int, nums2 []int) []int {
	mapChecker := make(map[int]bool)
	newArray := make(map[int]bool)
	keys := make([]int, 0, len(newArray))
	for _, value := range nums1 {
		mapChecker[value] = true
	}
	for _, num := range nums2 {
		if mapChecker[num] {
			newArray[num] = true
		}
	}
	for key, _ := range newArray {
		keys = append(keys, key)
	}
	return keys
}