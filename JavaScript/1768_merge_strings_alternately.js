/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let answer = "";
    let p1 = 0;
    let p2 = 0;
    while (p1 < word1.length && p2 < word2.length) {
        answer += word1[p1];
        answer += word2[p2];
        p1++;
        p2++;
    }
    return word1.length > word2.length ? answer + word1.slice(p1) : answer + word2.slice(p2);
};

