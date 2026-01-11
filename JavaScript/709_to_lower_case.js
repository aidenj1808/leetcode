/**
 * @param {string} s
 * @return {string}
 */
var toLowerCase = function(s) {
    let answer = "";
    for (let i = 0; i < s.length; i++) {
        const decimal = s.charCodeAt(i);
        if (decimal >= 65 && decimal <= 90) {
            console.log(String.fromCharCode(decimal + 32));
            answer += String.fromCharCode(decimal + 32);
        } else {
            answer += s[i];
        }
    }
    return answer;
};

