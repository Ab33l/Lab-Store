/*FizzBuzz
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Example 3:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
*/

func fizzBuzz(n int) []string {
    var mySlice []string
    for i := 1; i < n+1; i++{
        if i%3 == 0 && i%5 == 0{
            mySlice = append(mySlice, "FizzBuzz")
        }else if i%3 == 0{
            mySlice = append(mySlice, "Fizz")
        }else if i%5 == 0{
            mySlice = append(mySlice, "Buzz")
        }else{
            s := fmt.Sprintf("%d", i)
            mySlice = append(mySlice, s)
        }
    }
    return mySlice
}
