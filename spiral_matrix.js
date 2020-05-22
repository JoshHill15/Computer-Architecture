/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  if (matrix.length < 1 || matrix == null) {
    return []
  }

  const size = matrix[0].length * matrix.length
  const ans = []

  let left = 0
  let top = 0
  let right = matrix[0].length - 1
  let bottom = matrix.length - 1
  while (ans.length < size) {
    for (let i = left; i <= right; i++) {
      if (ans.length == size) return ans
      else ans.push(matrix[top][i])

    }

    top++

    for (let i = top; i <= bottom; i++) {
      if (ans.length == size) return ans
      else ans.push(matrix[i][right])
    }

    right--

    for (let i = right; i >= left; i--) {
      if (ans.length == size) return ans
      else ans.push(matrix[bottom][i])
    }

    bottom--

    for (let i = bottom; i >= top; i--) {
      if (ans.length == size) return ans
      else ans.push(matrix[i][left])
    }

    left++
  }
  return ans
};
let aa = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
let bb = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
const a = spiralOrder(aa)
console.log(a)
//[1,2,3,4,8,12,      16,15,14,13,9,5,       6,7,11,10]