/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let consistentWords = 0;
    for (const word of words) {
        let valid = true;
        for (char of word) {
            if (!allowed.includes(char)) {
                valid = false;
            }
        }

        if (valid) {
            consistentWords += 1;
        }
    }
    return consistentWords;
};

