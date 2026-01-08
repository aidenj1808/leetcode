/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x = 0;
    for (const operation of operations) {
        if (operation === "++X" || operation === "X++") {
            x += 1;
        } else {
            x -= 1;
        }
    }
    return x;
};

