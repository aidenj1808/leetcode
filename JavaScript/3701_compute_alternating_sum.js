/**
 * @param {number[]} nums
 * @return {number}
 */
var alternatingSum = function(nums) {
    let ret = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) {
            ret += nums[i];
        } else {
            ret -= nums[i];
        }
    }
    return ret;
};

