/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let runningSum = 0;
    let answer = [];
    for (const num of nums) {
        runningSum += num;
        answer.push(runningSum);
    }
    return answer;
};

