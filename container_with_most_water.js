/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0, right = height.length - 1;
    let max = 0;

    while (left < right) {
        let minH = Math.min(height[left], height[right]);
        let current = (right - left) * minH;
        if (current > max) max = current;
        if (minH == height[left]) left++;
        else right--;
    }

    return max;
};
