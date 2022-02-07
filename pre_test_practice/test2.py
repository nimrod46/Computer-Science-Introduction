def pairs2dict(lst):
    dict = {}
    for i in lst:
        if not i[0] in dict:
            dict[i[0]] = [i[1]]
        else:
            dict[i[0]].append(i[1])
    return dict


print(pairs2dict([(1, 2), (2, 3), (1, 4), (2, 5), (3, 5), (4, 1), (1, 7)]))


def get_one_number(lst):
    if len(lst) == 1:
        return lst[0]
    num = get_one_number(lst[1:])
    lenght = 0
    n = num
    while n != 0:
        lenght += 1
        n = n // 10

    return lst[0] * (10 ** lenght) + num


print(get_one_number([123, 45, 6789, 101112]))


def is_proper_subset(a, b):
    if len(a) >= len(b):
        return False
    for i in a:
        if i not in b:
            return False
    return True


print(is_proper_subset({1, 2, 3, }, {1, 2, 3, 4}))
print(is_proper_subset({1, 2, 3}, {1, 2, 3}))


def contains_subset(s):
    for a in s:
        for b in s:
            if is_proper_subset(a, b):
                return a, b

    return None


print(contains_subset([{1, 2, 3}, {1, 6}, {2, 3, 5}]))
print(contains_subset([{'one', 2, 3, 4}, {1, 6}, {2, 3, 4}]))


def num_ab(s):
    if len(s) <= 1:
        return 0
    c = 0
    if s[:2] == "ab":
        c = 1
    return c + num_ab(s[1:])


print(num_ab('abracadabra abanibi'))


def is_tournament(table):
    n = len(table)
    for i in range(n):
        for j in range(len(table[i])):
            if table[i][j] >= n or table[i][j] < 0:
                return False
            if table[i][j] == i:
                return False
            if i not in table[table[i][j]]:
                return False
    return True


print(is_tournament([[1, 2, 3], [0], [0, 3], [2, 0]]))
print(is_tournament([[1, 2, 3], [2, 0], [0, 1, 3], [2, 0]]))
print(is_tournament([[1, 2], [2, 0, 3], [0, 1, 3], [1, 2]]))
import math


class Point:
    """ a point in the plane """

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def distance(self, other):
        """ returns the distance between two points """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Circle:
    def __init__(self, center, radius):
        self.validate_center(center)
        self.validate_radius(radius)
        self.__radius = radius
        self.__center = center

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, value):
        self.validate_center(value)
        self.__center = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.validate_radius(value)
        self.__radius = value

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius

    def contains(self, other):
        return self.__center.distance(other.center) + other.radius <= self.__radius

    def validate_center(self, center):
        if not isinstance(center, Point):
            raise TypeError("Center must be a Point object!")

    def validate_radius(self, radius):
        if not isinstance(radius, float):
            raise TypeError("Radius must be a float!")
        if radius <= 0:
            raise ValueError("Radius must be a positive number!")


center = Point(0, 0)
center1 = Point(0, 3)
circle = Circle(center, 5.0)
smallCircle = Circle(center1, 2.0)
print(circle.contains(smallCircle))


def transpose(mat):
    return [[mat[c][r] for c in range(len(mat))] for r in range(len(mat[0]))]


def is_latin(mat):
    n = len(mat)
    mat_t = transpose(mat)
    base = {i for i in range(1, n + 1)}
    for i in range(n):
        if len(set(mat[i])) != n or len(set(mat_t[i])) != n:
            return False
        if not set(mat[i]).issubset(base) or not set(mat_t[i]).issubset(base):
            return False
    return True


print()

print((1, 3, 2) in {(1, 3), 2, 3, 1})

print(is_latin(transpose([[1, 2, 3], [2, 3, 1], [3, 1, 2]])))

s = {1}
s.add(2)
print({1} | {2})


def div(k, n=1):
    if k <= n:
        return {n}
    if k % n == 0:
        return {n} | div(k, n + 1)
    return div(k, n + 1)


print(div(24))
