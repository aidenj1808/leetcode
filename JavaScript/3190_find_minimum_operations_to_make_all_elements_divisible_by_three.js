/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    let operations = 0;
    for (const num of nums) {
        if (num % 3 !== 0) {
            operations += Math.min(num % 3, 3 - (num % 3));
        }
    }
    return operations;
};

