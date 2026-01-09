/**
 * @param {number[]} order
 * @param {number[]} friends
 * @return {number[]}
 */
var recoverOrder = function(order, friends) {
    let ret = [];
    let friendsSet = new Set(friends);
    for (const participant of order) {
        if (friendsSet.has(participant)) {
            ret.push(participant);
        }
    }
    return ret;
};

