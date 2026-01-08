/**
 * @param {number} n
 * @return {number}
 */
var smallestEvenMultiple = function(n) {
    let ret;
    if (n % 2 !== 0) {
        ret = n * 2;
    } else {
        ret = n;
    }
    return ret;
};

