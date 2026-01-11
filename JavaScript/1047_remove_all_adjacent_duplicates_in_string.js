/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
    let stack = [];
    for (const char of s) {
        if (stack.at(-1) !== char) {
            stack.push(char);
        } else {
            stack.pop();
        }
    }
    return stack.join('');
};

