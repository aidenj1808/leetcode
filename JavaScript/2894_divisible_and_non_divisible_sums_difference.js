/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    let num1 = 0;
    let num2 = 0;
    for (let x = 1; x < n + 1; x++) {
        if (x % m !== 0) {
            num1 += x;
        } else {
            num2 += x;
        }
    }
    return num1 - num2;
};

