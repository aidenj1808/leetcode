/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} multiplier
 * @return {number[]}
 */
var getFinalState = function(nums, k, multiplier) {
    for (let x = 0; x < k; x++) {
        const min = Math.min(...nums);
        nums[nums.indexOf(min)] *= multiplier;
    }
    return nums;
};

