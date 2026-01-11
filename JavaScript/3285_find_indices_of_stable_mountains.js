/**
 * @param {number[]} height
 * @param {number} threshold
 * @return {number[]}
 */
var stableMountains = function(height, threshold) {
    let answer = [];
    for (let i = 1; i < height.length; i++) {
        if (height[i - 1] > threshold) {
            answer.push(i);
        }
    }
    return answer;
};

