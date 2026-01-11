/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let answer = [];
    let smallerNumbersCount = 0;
    for (const num1 of nums) {
        for (const num2 of nums) {
            if (num1 > num2) {
                smallerNumbersCount++;
            }
        }
        answer.push(smallerNumbersCount);
        smallerNumbersCount = 0;
    }
    return answer;
};

