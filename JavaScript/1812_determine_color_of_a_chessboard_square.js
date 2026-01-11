/**
 * @param {string} coordinates
 * @return {boolean}
 */
var squareIsWhite = function(coordinates) {
    const square = coordinates.charCodeAt(0) + parseInt(coordinates[1]);
    return square % 2 === 1 ? true : false;
};

