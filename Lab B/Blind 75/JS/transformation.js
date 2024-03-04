/*Functional Programming (no state, no variable) - Reuse of class, methods
Strategy design pattern - Open-Closed Principle [Closed to change but open for extension]
Transform over each element in an array
Input: arr = [1,2,3], fn = function plusone(n) { return n + 1; }
Output: [2,3,4]
Explanation:
const newArray = map(arr, plusone); // [2,3,4]
The function increases each value in the array by one. 
*/
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const res = [];
    for(let i=0; i < arr.length; i++){
        res[i] = fn(arr[i], i);
    }
    return res;
};
