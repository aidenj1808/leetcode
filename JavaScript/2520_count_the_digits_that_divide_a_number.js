/**
 * @param {number} num
 * @return {number}
 */
var countDigits = function(num) {
    let divisibleDigits = 0;
    let digits = String(num).split('');
    for (const digit of digits) {
        if (num % digit === 0) {
            divisibleDigits += 1;
        }
    }
    return divisibleDigits;
};

