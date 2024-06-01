'''
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  
'''
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0 #Number of steps
        carry = 0 #Handles the addition of 1 to the next higher bit when needed.
        n = len(s) - 1 
        # Loop from final to first character but exclude first character
        for i in range(n, 0, -1):
            # Check if the current bit plus carry equals 1
            if int(s[i]) + carry == 1:
                carry = 1 # Set carry to 1 (we need to add 1 in the next higher bit), 
                steps += 2 # It takes 2 steps: 1 to make the bit 0 (subtract 1) and 1 to divide by 2
            else:
                steps += 1 # If the current bit plus carry equals 0, it takes 1 step to divide by 2
        return steps + carry

        
