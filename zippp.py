import gzip
import pickle

# class Student:
#     def __init__(self,name,age,grades):
#         self.name=name
#         self.age=age
#         self.grades = grades


# stident = Student("ayya", 30, [2,3,4])


# with open ("p8.pkl", "wb") as f:
#     pickle.dump(stident, f)
    
# with open ("p8.pkl", "rb") as f:
#     a = pickle.load(f)
    
# print(a.name)





# class Student:
#     def __init__(self,name,age,grades):
#         self.name=name
#         self.age=age
#         self.grades = grades

# stident = Student("ayya", 30, [2,3,4])

# data = pickle.dumps(stident)
# upload=pickle.loads(data)

# print(type(data))






# class Student:
#     def __init__(self,name,age,grades, secret):
#         self.name=name
#         self.age=age
#         self.grades = grades
#         self.secret = secret
        
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state["secret"]
#         state["_version"]=1
#         return state
        
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         self.secret=""
    
# stident = Student("ayya", 30, [2,3,4], None)


# with open ("p8.pkl", "wb") as f:
#     pickle.dump(stident, f)
    
# with open ("p8.pkl", "rb") as f:
#     a = pickle.load(f)
    
# print(a.secret)



# class Group:
#     def __init__(self,name):
#         self.name=name
        
# class Student:
#     def __init__(self,group,name):
#         self.name=name
#         self.group=group
        
# group=Group("P-8-24")
# st=Student(group, "Ayyf")

# with open ("p8.pkl", "wb") as f:
#     pickle.dump(st, f)
    
# with open ("p8.pkl", "rb") as f:
#     st1 = pickle.load(f)
    
# print(st1.name,st1.group.name)













import json

# class Student:
#     def __init__(self,name, age, grades):
#         self.name=name
#         self.age=age
#         self.grades=grades

#     def to_dict(self):
#         return{
#         "name": self.name,
#         "age":self.age,
#         "grades": self.grades
#     }
    
# def to_def(obj):
#     if isinstance(obj, Student):
#         return obj.to_dict()
# raise TypeError(f"Обьект даукн")
    
    
    
#     @classmethod
#     def from_dict(cls,st):
#         return cls(
#             name=st["name"],
#         age=st ["age"],
#         grades=st["grades"]
# )


from dataclasses import dataclass, asdict

@dataclass
class Student:
    name:str
    age:int
    grades:list
    
student=Student("g",40, [4,2,3])

st_to_dict=asdict(student)

with open("st8.json","w",encoding="utf-8") as file:
    json.dump(st_to_dict, file, ensure_ascii=False, indent=2)