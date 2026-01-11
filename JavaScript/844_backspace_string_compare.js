/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    let sStack = [];
    for (const char of s) {
        if (char !== '#') {
            sStack.push(char);
        } else {
            sStack.pop();
        }
    }

    let tStack = [];
    for (const char of t) {
        if (char !== '#') {
            tStack.push(char);
        } else {
            tStack.pop();
        }
    }
    return sStack.join('') === tStack.join('');
};

