/**
 * @param {string} s
 * @return {number}
 */
var minLength = function(s) {
    let stack = [];
    for (const char of s) {
        stack.push(char);
        if (stack.length > 1 &&
            stack.at(-2) + stack.at(-1) === "AB" ||
            stack.at(-2) + stack.at(-1) === "CD"
        ) {
            stack.pop();
            stack.pop();
        }

    }
    return stack.length;
};

