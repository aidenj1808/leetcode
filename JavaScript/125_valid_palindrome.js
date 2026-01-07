/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let sAlphanumeric = "";
    for (char of s) {
        if (/[a-zA-Z0-9]/.test(char)) {
            sAlphanumeric += char.toLowerCase();
        }
    }

    let left = 0;
    let right = sAlphanumeric.length - 1;
    while (left < right) {
        if (sAlphanumeric[left] !== sAlphanumeric[right]) {
            return false;
        }
        left += 1;
        right -= 1;
    }
    return true;
};

