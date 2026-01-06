/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSneakyNumbers = function(nums) {
    let ret = [];
    nums.sort();
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            ret.push(nums[i]);
        }
    }
    return ret;
};

