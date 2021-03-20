class FenWickTree(object):
    def __init__(self, n):
        self._n = n
        self.data = [0] * n


    def add(self, i, x):
        assert 0 <= i < self._n
        i += 1
        while i < self._n:
            self.data[i-1] += x
            i += i & -i

    def sum(self, l, r):
        assert 0 <= l <= r < self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i-1]
            i -= i & -i
        return s

if __name__ =='__main__':
    N = 10
    fw = FenWickTree(N)
