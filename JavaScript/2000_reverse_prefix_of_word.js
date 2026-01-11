/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    const firstIndex = word.indexOf(ch);
    const reverse = word.slice(0, firstIndex + 1).split('').reverse().join('');
    return reverse + word.slice(firstIndex + 1);
};

