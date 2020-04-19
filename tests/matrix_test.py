import unittest
import matrix as m


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
    #a[(2, 0)] = 3
    #a[(2, 1)] = 6

    b = m.Matrix(2, 3)
    b[(0, 0)] = 2
    b[(0, 1)] = 4

    c = m.Matrix(2, 3)
    c[(0, 0)] = 4
    c[(0, 1)] = 2

    def test_add(self):
        #try:
            #a = self.a
            #self.a += self.c
        #except Exception:
            #assert True == True
        d = self.c + self.b
        assert d[(0, 0)] == 6 == d[(0, 1)]


if __name__ == '__main__':
    unittest.main()
