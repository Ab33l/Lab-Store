/*
Minimum Common Value - Find least common value in two arrays
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
*/

func getCommon(nums1 []int, nums2 []int) int {
	counts := make(map[int]bool)
	for _, value := range nums1 {
		counts[value] = true
	}
	for _, num := range nums2 {
		if counts[num] && num > 0 {
			return num
		}
	}
	return -1
}