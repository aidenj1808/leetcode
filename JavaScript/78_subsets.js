/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const n = nums.length;
    let solution = [];
    let result = [];

    function backtrack(i) {
        if (i == n) {
            result.push(Array.from(solution));
            return;
        }

        backtrack(i + 1);

        solution.push(nums[i]);
        backtrack(i + 1);
        solution.pop();
    }

    backtrack(0);
    return result; 
};

