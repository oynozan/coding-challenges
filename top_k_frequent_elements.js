/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let obj = {};
    let ans = [];

    for (let num of nums) {
        if (!obj?.[num]) obj[num] = 1;
        else obj[num] += 1;
    }

    for (let i = 0; i < k; i++) {
        let max = 0;
        for (let j of Object.values(obj)) {
            if (j > max) max = j;
        }
        for (let j of Object.keys(obj)) {
            if (obj[j] == max) {
                ans.push(j);
                delete obj[j];
                break;
            }
        }
    }

    return ans.sort();
};