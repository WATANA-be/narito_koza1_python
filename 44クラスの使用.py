members = {}
class Student:
    def __init__(self,name):
        self.name = name
        self.score = {}

    def add_score(self,subject_name,point):
        self.score[subject_name] = point

    def get_score(self,subject_name):
        return self.score.get(subject_name,'その強化はまだ')

members['narito'] = Student('narito')
members['satou'] = Student('satou')



saitou = Student('saitou')
saitou.add_score('math',100)
print(saitou.score)
print(members)

members['narito'].add_score('eng',100)
print(members)
        