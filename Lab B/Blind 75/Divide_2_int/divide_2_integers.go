/*
Input: 10/3 = 3.333 
Output: 3 (Truncated to 3)
Input: 7/-3 = -2.333
Output: -2 (Truncated to -2)
Input: 15/2 = 7.5
Output: 7 (Truncated to 7)
*/
func divide(dividend int, divisor int) int {
    if (dividend == -2147483648 && divisor == -1){
        return 2147483647
    }else{
        var f = dividend/divisor
        var z int = int(f)
        return z
    }
}
