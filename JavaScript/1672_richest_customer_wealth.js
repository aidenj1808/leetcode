/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let richestCustomer = 0;
    for (const customerAccounts of accounts) {
        let totalMoney = 0;
        for (const account of customerAccounts) {
            totalMoney += account;
        }
        richestCustomer = Math.max(richestCustomer, totalMoney);
    }
    return richestCustomer;
};

