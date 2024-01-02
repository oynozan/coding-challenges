/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows == 1) return s;
    let hashmap = {}

    for (let i = 1; i < numRows + 1; i++) hashmap[i] = "";

    let mode = "v", // Vertical: 'v' || Diagonal: 'd'
        modeCounter = 0;
    for (let i = 0; i < s.length; i++) {
        // Set the mode
        modeCounter++;

        if (mode == "v") {
            // Vertical
            hashmap[modeCounter] += s[i]
        } else {
            // Diagonal
            hashmap[(numRows - modeCounter)] += s[i]
        }

        if (
            ((mode == "v" && modeCounter == numRows) ||
            (mode == "d" && modeCounter == numRows - 2)) &&
            numRows > 2
        ) {
            modeCounter = 0;

            // Change the mode
            if (mode == "v") mode = "d";
            else mode = "v";
        }

        else if (modeCounter == numRows) modeCounter = 0
    }

    let result = "";
    for (let key of Object.keys(hashmap)) {
        result += hashmap[key];
    }

    return result;
};
