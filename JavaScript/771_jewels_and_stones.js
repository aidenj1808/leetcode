/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    let jewelStonesCount = 0;
    let jewelsSet = new Set(jewels);
    for (const stone of stones) {
        if (jewelsSet.has(stone)) {
            jewelStonesCount += 1;
        }
    }
    return jewelStonesCount;
};

