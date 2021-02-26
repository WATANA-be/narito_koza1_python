print(type(1))
print(type('moji'))
print(type([1]))

class Student:
    def __init__(self,name):
        self.name = name

a = Student('watana')#返すものをインスタンス
print(a.name)