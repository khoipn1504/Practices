class Vector():

    def __init__(self, d):
        self._coords = [0]*d

    def __len__(self):
        return self._coords

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):          # dựa trên phương thức __len__
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]+other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other            # dựa trên phương thức __eq__

    def __str__(self):
        return '<'+str(self._coords)[1:-1]+'>'


a=Vector(4)
a.__setitem__(1,34)
print(a)
