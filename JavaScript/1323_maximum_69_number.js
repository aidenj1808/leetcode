/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function(num) {
    let first_six_index = -1;
    let digits = String(num).split('');
    for (const [i, digit] of digits.entries()) {
        if (digit === '6') {
            first_six_index = i;
            break;
        }
    }

    if (first_six_index === -1) {
        return num;
    } else {
        digits[first_six_index] = '9';
        return parseInt(digits.join(""));
    }
};

