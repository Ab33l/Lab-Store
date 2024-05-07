/*
Like car on journey (move one element ata time), if current gas is less than what is in the tank we subtract by 1 unit, if gas in next element is more than what is in the car then we update car gas amount to new value
Continue till gas in car ends or we remain with surplus
Input: [2,3,1,1,4]
Output: true
Input: [3,2,1,0,4]
Output: false
*/
func canJump(nums []int) bool {
    var gas int = 0
    for i := 0; i < len(nums); i++{
        if gas < 0{
            return false
        }else if nums[i] > gas{
            gas = nums[i]
        }
        gas = gas - 1
    }
    return true
}
