/*
Reduce Transformation (aggregator)
Input: 
nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0
Output: 10
Explanation:
initially, the value is init=0.
(0) + nums[0] = 1
(1) + nums[1] = 3
(3) + nums[2] = 6
(6) + nums[3] = 10
The final answer is 10.
*/
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    newVal = init;
    if(nums.length == 0){
        return init;
    }

    for(let i=0; i < nums.length; i++){
        newVal = fn(newVal, nums[i]);
    }
    return newVal; 
};