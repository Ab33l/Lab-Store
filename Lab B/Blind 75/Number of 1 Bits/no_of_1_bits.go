/*Input: n = 00000000000000000000000000001011
Output: 3
Input: n = 11111111111111111111111111111101
Output: 31
*/

func hammingWeight(num uint32) int {
	res := 0
	for num > 0 {
		num = num & (num - 1)
		res += 1
	}
	return res
}