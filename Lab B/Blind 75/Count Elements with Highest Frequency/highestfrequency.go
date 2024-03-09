/*
Count Elements With Maximum Frequency
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
*/
func maxFrequencyElements(nums []int) int {
    counts := make(map[int]int)
    var maxVal, countVal int
    for _, num := range nums{
        counts[num]++
    }
    for _,value := range counts{
        if value > maxVal{
            maxVal = value
            countVal = 1
        }else if value == maxVal{
            countVal++
        }
    }
    return countVal * maxVal
}