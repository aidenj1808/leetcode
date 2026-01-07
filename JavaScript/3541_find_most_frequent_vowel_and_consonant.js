/**
 * @param {string} s
 * @return {number}
 */
var maxFreqSum = function(s) {
    let letterCounts = new Map();
    for (char of s) {
        if (!letterCounts.has(char)) {
            letterCounts.set(char, 0);
        }
        letterCounts.set(char, letterCounts.get(char) + 1);
    }

    let vowelMax = 0;
    let consonantMax = 0;
    for ([char, count] of letterCounts) {
        if ("aeiou".includes(char)) {
            vowelMax = Math.max(vowelMax, count);
        } else {
            consonantMax = Math.max(consonantMax, count);
        }
    }
    return vowelMax + consonantMax;
};

