/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const closeToOpen = new Map([
        [")", "("],
        ["]", "["],
        ["}", "{"]
    ]);
    let stack = [];
    for (char of s) {
        if ("([{".includes(char)) {
            stack.push(char);
        } else if (closeToOpen.get(char) === stack.at(-1)) {
            stack.pop();
        } else {
            return false;
        }
    }
    return stack.length === 0;
};

