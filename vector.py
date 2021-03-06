#!/usr/bin/python

import math
import re

inc = 23.4 * math.pi / 180

def make_vector_from_list(l):
    return Vector(l[0], l[1], l[2])

class Vector:

    def __init__(self, v1, v2, v3):

        self.v1 = 1.0 * v1
        self.v2 = 1.0 * v2
        self.v3 = 1.0 * v3

    def __mul__(self, n):
        return Vector(n* self.v1, n* self.v2, n* self.v3)

    def __add__(self, other):
        return Vector(self.v1 + other.v1, self.v2 + other.v2, self.v3 + other.v3)

    def __sub__(self, other):
        return Vector(self.v1 - other.v1, self.v2 - other.v2, self.v3 - other.v3)

    def __neg__(self):
        return Vector(-self.v1, -self.v2, -self.v3)

    def __getitem__(self, i):
        return self.vector()[i]

    @staticmethod
    def eclipticToEquatorial(v):
        v1 = v[0]
        v2 = math.cos(inc) * v[1] - math.sin(inc) * v[2]
        v3 = math.cos(inc) * v[2] + math.sin(inc) * v[1]
        return Vector(v1, v2, v3)
    @staticmethod
    def equatorialToEcliptic(v):
        v1 = v[0]
        v2 = math.cos(inc) * v[1] + math.sin(inc) * v[2]
        v3 = math.cos(inc) * v[2] - math.sin(inc) * v[1]
        return Vector(v1, v2, v3)
  
    @staticmethod
    def createFromString(s):
        v = [float(a) for a in re.findall('[\-\d\.]+', s)]
        return Vector(v[0], v[1], v[2])

    def vector(self):
        return [self.v1, self.v2, self.v3] 

    def X(self):
        return self.v1

    def Y(self):
        return self.v2

    def Z(self):
        return self.v3

    def negate(self):
        self.v1 = -self.v1
        self.v2 = -self.v2
        self.v3 = -self.v3
        return self

    def norm(self):
        m = self.magnitude()
        if m > 0.0:
            return Vector(self.v1/m, self.v2/m, self.v3/m)
        else:
            return self


    def normalize(self):
        self = self.norm()
        return self
        

    def magnitude(self):
        return math.sqrt(self.v1 ** 2 + self.v2 **2 + self.v3**2)

    def scalarproduct(self, other):
        return self.v1 * other.v1 + self.v2 * other.v2 + self.v3 * other.v3

    def vectorproduct(self, other):
        return Vector(self.v2*other.v3 - self.v3*other.v2, self.v3*other.v1 - self.v1*other.v3, self.v1*other.v2 - self.v2*other.v1)

    def anglebetween(self, other):
        v1 = self.norm()
        v2 = other.norm()
        return math.acos(v1.scalarproduct(v2))

    def __str__(self):
  
        return '(' + str(self.v1) + ', ' + str(self.v2) + ', ' + str(self.v3) + ')'

    def __repr__(self):
        return str(self)

