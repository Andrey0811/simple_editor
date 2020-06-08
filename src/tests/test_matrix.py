import unittest
from src.geometry import matrix as m


class Matrix_Test(unittest.TestCase):
    e = m.Matrix(4, 4)
    e[(0, 0)] = 1
    e[(1, 1)] = 1
    e[(2, 2)] = 1

    a = m.Matrix(3, 4)
    a[(0, 0)] = 1
    a[(0, 1)] = 2
    a[(0, 2)] = 3
    a[(1, 0)] = 4
    a[(1, 1)] = 5

    b = m.Matrix(2, 3)
    b[(0, 0)] = 2
    b[(0, 1)] = 4
    b[(1, 0)] = 0
    b[(1, 1)] = 0

    c = m.Matrix(2, 3)
    c[(0, 0)] = 4
    c[(0, 1)] = 2
    c[(1, 0)] = 0
    c[(1, 1)] = 0

    def test_init(self):
        self.assertRaises(ValueError, m.Matrix, 0, 0)

    def test_is_quadratic(self):
        assert self.a.is_quadratic() == False
        assert self.e.is_quadratic() == True

    def test_copy(self):
        temp = self.e.copy()
        assert self.e.is_quadratic() == temp.is_quadratic()
        assert self.e.cols_count() == temp.cols_count()
        assert self.e.rows_count() == temp.rows_count()
        assert self.e[(0, 0)] == temp[(0, 0)]

    def test_rows_count(self):
        assert self.a.rows_count() == 4

    def test_col_count(self):
        assert self.a.cols_count() == 3

    def test_get_row(self):
        self.assertRaises(ValueError, self.a.get_row, 10)
        assert isinstance(self.a.get_row(0), list)
        assert self.a.get_row(0)[0] == self.a[(0, 0)]

    def test_get_col(self):
        self.assertRaises(ValueError, self.a.get_col, 10)
        assert isinstance(self.a.get_col(0), list)
        assert self.a.get_col(0)[0] == self.a[(0, 0)]

    def test_add(self):
        self.assertRaises(ValueError, self.a.__add__, self.c)
        # assert self.b.__add__(self.c)[(0, 0)] == 6
        # assert self.b.__add__(self.c)[(0, 1)] == 6

    def test_sub(self):
        self.assertRaises(ValueError, self.a.__add__, self.c)

    def test_mul(self):
        self.assertRaises(ValueError, self.a.__mul__, self.b)
        self.assertRaises(ValueError, self.a.__mul__, '')

    def test_transpose(self):
        pass

    def test_determinate(self):
        self.assertRaises(ValueError, self.a.determinate)
        temp = self.e.determinate()
        assert temp == 1

    def test_minors_row(self):
        pass

    def test_minors_col(self):
        pass

    def test_minor(self):
        pass

    def test_reverse(self):
        pass


if __name__ == '__main__':
    unittest.main()
