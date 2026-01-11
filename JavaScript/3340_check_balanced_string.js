/**
 * @param {string} num
 * @return {boolean}
 */
var isBalanced = function(num) {
    let evenSum = 0;
    let oddSum = 0;
    for ([i, digit] of num.split('').entries()) {
        digit = parseInt(digit);
        if (i % 2 === 0) {
            evenSum += digit;
        } else {
            oddSum += digit;
        }
    }
    return evenSum === oddSum;
};

