
class A():
    def __init__(self, color, size):
        self.color = color
        self. size = size
    def __str__(self):
        return f"color = {self.color} size = {self.size} "

class B():
    def __init__(self, aa):
        self.aa = aa
    def __str__(self):
        return f"aa = {self.aa}"


a = A("green",15)
print(a)
b = B(a)
print(b)