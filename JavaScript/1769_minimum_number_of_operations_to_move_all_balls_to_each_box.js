/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function(boxes) {
    let ans = new Array(boxes.length).fill(0);
    for (let i = 0; i < boxes.length; i++) {
        for (const [j, box] of boxes.split('').entries()) {
            if (box == '1') {
                ans[i] += Math.abs(i - j);
            }
        }
    }
    return ans;
};

