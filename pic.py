import pickle

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
p1 = Point(3,4)

with open("point8.pkl", "wb") as f:
    pickle.dump(p1,f)

with open("point8.pkl", "rb") as f:
    loaded = pickle.load(f)
    
print(p1.x, p1.y)
print(loaded.x, loaded.y)

points=[Point(3,4),Point(5,4),Point(7,4)]

with open("point8.pkl","wb") as file:
    pickle.dump(points,file)

with open("point8.pkl","rb") as file:
    loaded_p=pickle.load(file)

for i in loaded_p:
    print(i.x,i.y)







    
import json
student = {"name":"B","age":30, "grades": [3,4,5]}

with open("st8.json", "w", encoding="utf-8") as f:
    json.dump(student, file,ensure_ascii=False, indent=2)
    
with open("st8.json","r",encoding="utf-8") as file:
    loaded=json.load(file)
print(loaded)

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        
    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        }
    
    @classmethod
    def from_dict(cls,st):
        return cls(
            name=st["name"],
            age=st["age"],
            grades=st["grades"]
            )
    
st1 = Student("п",40,[4,2,3])

with open("st8.json", "w", encoding="utf-8") as f:
    json.dump(st1.to_dict(), file, ensure_ascii=False, indent=2)