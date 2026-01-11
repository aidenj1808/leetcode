/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    const filesOrDirectories = path.split('/');
    let stack = [];
    for (const fileOrDirectory of filesOrDirectories) {
        if (fileOrDirectory === '' || fileOrDirectory == '.') {
            continue;
        }

        stack.push(fileOrDirectory);
        if (fileOrDirectory === "..") {
            stack.pop();
            stack.pop();
        }
    }
    return '/' + stack.join('/');
};

