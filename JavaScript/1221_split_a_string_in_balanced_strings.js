/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let balance = 0;
    let ret = 0;
    for (const char of s) {
        if (char === 'L') {
            balance += 1;
        } else {
            balance -= 1;
        }

        if (!balance) {
            ret += 1;
        }
    }
    return ret;
};

