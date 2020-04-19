import math
import vector as v


class Matrix:

    def __init__(self, rows, cols, create_identity=True):
        if rows < 2 or cols < 2:
            raise Exception('Invalid Matrix')
        self.rows = rows
        self.cols = cols
        self.m = [[0.0] * rows for x in range(cols)]

        if self.is_quadratic() and create_identity:
            for i in range(self.rows):
                self.m[i][i] = 1.0

    def is_quadratic(self) -> bool:
        return self.rows == self.cols

    def copy(self) -> 'Matrix':
        r = Matrix(self.rows, self.cols, False)
        for i in range(self.rows):
            for j in range(self.cols):
                r.m[i][j] = self.m[i][j]
        return r

    def __getitem__(self, a):
        row, col = a[0], a[1]
        if self.rows > row and self.cols > col:
            return self.m[row][col]
        else:
            raise Exception('Invalid Matrix')

    def __setitem__(self, a, val):
        row, col = a[0], a[1]
        if self.rows > row and self.cols > col:
            self.m[row][col] = val
        else:
            raise Exception('Invalid Matrix')

    def rows_count(self) -> int:
        return len(self.m)

    def cols_count(self) -> int:
        return len(self.m[0])

    def get_row(self, i) -> list:
        if i < self.rows:
            return self.m[i]
        else:
            raise Exception('Invalid Matrix')

    def get_col(self, j) -> list:
        if j < self.cols:
            return [row[j] for row in self.m]
        else:
            raise Exception('Invalid Matrix')

    def __add__(self, right: 'Matrix') -> 'Matrix':
        if self.rows == right.rows and self.cols == right.cols:
            temp = Matrix(self.rows, self.cols, False)
            for i in range(self.rows):
                for j in range(self.cols):
                    temp.m[i][j] = self.m[i][j] + right.m[i][j]
            return temp
        else:
            raise Exception('Invalid Matrix')

    def __sub__(self, right: 'Matrix') -> 'Matrix':
        if self.rows == right.rows and self.cols == right.cols:
            temp = Matrix(self.rows, self.cols, False)
            for i in range(self.rows):
                for j in range(self.cols):
                    temp.m[i][j] = self.m[i][j] - right.m[i][j]
            return temp
        else:
            raise Exception('Invalid Matrix')

    def __mul__(self, right: 'Matrix'):
        if isinstance(right, Matrix):
            if self.cols == right.rows:
                temp = Matrix(self.rows, right.cols, False)
                for i in range(self.rows):
                    for j in range(right.cols):
                        for k in range(self.cols):
                            temp.m[i][j] += self.m[i][k] * right.m[k][j]
                return temp
            else:
                raise Exception('Invalid Matrix')
        elif isinstance(right, v.Vector):
            temp = v.Vector()
            add_x = add_y = add_z = 0.0
            if self.rows == self.cols == 4:
                add_x = self.m[0][3]
                add_y = self.m[1][3]
                add_z = self.m[2][3]
            temp.x = self.m[0][0] * right.x + self.m[0][1] * right.y + self.m[0][2] * right.z + add_x
            temp.y = self.m[1][0] * right.x + self.m[1][1] * right.y + self.m[1][2] * right.z + add_y
            temp.z = self.m[2][0] * right.x + self.m[2][1] * right.y + self.m[2][2] * right.z + add_z

            if self.rows == self.cols == 4:
                w = self.m[3][0] * right.x + self.m[3][1] * right.y + self.m[3][2] * right.z + self.m[3][3]
                if w != 1 and w != 0:
                    temp.x /= w
                    temp.y /= w
                    temp.z /= w
            return temp
        elif isinstance(right, int) or isinstance(right, float):
            temp = Matrix(self.rows, self.cols, False)
            for i in range(self.rows):
                for j in range(self.cols):
                    temp.m[i][j] = self.m[i][j] * right
            return temp
        else:
            raise Exception('Invalid Matrix')

    def transpose(self) -> 'Matrix':
        temp = Matrix(self.cols, self.rows, False)
        for j in range(self.cols):
            for i in range(self.rows):
                temp.m[j][i] = self.m[i][j]
        return temp

    def determinate(self):
        if not self.is_quadratic():
            raise Exception('Invalid Matrix')

        if self.rows == 2:
            return self.m[0][0] * self.m[1][1] - self.m[0][1] * self.m[1][0]

        return self.minors_row(0)

    def minors_row(self, row):
        assert (row < self.rows)
        d = 0
        for col in range(self.cols):
            d += (-1) ** (row + col) * self.m[row][col] * self.minor(row, col).determinate()
        return d

    def minors_col(self, col):
        assert (col < self.cols)
        d = 0
        for row in range(self.rows):
            d += (-1) ** (row + col) * self.m[row][col] * self.minor(row, col).determinate()
        return d

    def minor(self, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            raise Exception('Invalid Matrix')
        temp = Matrix(self.rows - 1, self.cols - 1)
        minor_row = minor_col = 0
        for self_row in range(self.rows):
            if not self_row == i:
                for self_col in range(self.cols):
                    if not self_col == j:
                        temp.m[minor_row][minor_col] = self.m[self_row][self_col]
                        minor_col += 1

                minor_col = 0
                minor_row += 1

        return temp

    def reverse(self):
        if not self.is_quadratic():
            raise Exception('Invalid Matrix')
        else:
            N = self.cols
            temp = Matrix(N, N)
            mo = self.copy()
            for col in range(N):
                if mo.m[col][col] == 0:
                    big = col
                    for row in range(N):
                        if math.fabs(mo.m[row][col]) > math.fabs(mo.m[big][col]):
                            big = row
                    if big != col:
                        for j in range(N):
                            mo.m[col][j] = mo.m[big][j]
                            mo.m[big][j] = mo.m[col][j]
                            temp.m[col][j], temp.m[big][j] = temp.m[big][j], temp.m[col][j]

                for row in range(N):
                    if row != col:
                        k = mo.m[row][col] / mo.m[col][col]
                        if k != 0:
                            for j in range(N):
                                mo.m[row][j] -= k * mo.m[col][j]
                                temp.m[row][j] -= k * temp.m[col][j]

                            mo.m[row][col] = 0

            for row in range(N):
                for col in range(N):
                    temp.m[row][col] /= mo.m[row][row]

            return temp
