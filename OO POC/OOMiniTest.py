class Supertest():
    type = "oer"
    def __init(self, name, a, b, identification):
        self.name = name
        self.a = a
        self.b = b
        self.idn = identification
    def __str__(self):
        return f"{self.name}-{self.idn} van type {self.type} heeft {self.a} en {self.b} "

class FeatureClass():
    def __init__(self,nr):
        self.nr = nr
    def __repr__(self):
        return f" {self.nr}-toedeloe"
    pass


class Subtest(Supertest):
    type = "subclass"
    extra = "zzz"
    def __init__(self, l):
        self.feature_reeks = []
        for i in range(l):
            self.feature = FeatureClass(i)
            self.feature_reeks.append(self.feature)
    def drukaf(self):
        print(f"{self.name} heeft niet {self.a} maar wel {self.b} en {self.extra} en {self.feature_reeks}")
    pass



jan_01 = Supertest()
jan_01.name = "Jan"
jan_01.a = "reeks a"
jan_01.b = "reeks b"
jan_01.idn = 1
print(jan_01)

f_01 = FeatureClass(45)
print(f_01)

piet_01 = Subtest(7)
piet_01.name = "Piet"
piet_01.a = "reeks y"
piet_01.b = "reeks z"
piet_01.idn = 2
piet_01.extra = "vakantie"
# piet_01.reekslengte = 3
piet_01.drukaf()
print(piet_01)

