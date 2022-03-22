class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)];
        cnt = 1;
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        d = 0;
        row = 0;
        col = 0;
        while (cnt <= n * n):
            result[row][col] = cnt;
            cnt += 1;
            r = (row + dir[d][0]) % n;
            c = (col + dir[d][1]) % n;

            # change direction if next cell is non zero
            if (result[r][c] != 0):
                d = (d + 1) % 4;

            row += dir[d][0];
            col += dir[d][1];
        return result;
