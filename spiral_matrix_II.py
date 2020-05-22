

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        grid = [[0] * n for _ in range(n)]

        row_start = 0
        row_last = n - 1
        col_end = n - 1
        col_begin = 0
        count = 1

        while row_start <= row_last and col_begin <= col_end:

            for i in range(col_begin, col_end + 1):
                grid[row_start][i] = count
                count += 1

            row_start += 1
            for i in range(row_start, row_last + 1):
                grid[i][col_end] = count
                count += 1

            col_end -= 1

            for i in range(col_end, col_begin - 1, -1):
                grid[row_last][i] = count
                count += 1

            row_last -= 1

            for i in range(row_last, row_start - 1, -1):
                grid[i][col_begin] = count
                count += 1

            col_begin += 1

        return grid


sol = Solution()
a = sol.generateMatrix(3)
print(a)
