'''class Ainwik:
    branch=["CS","IT"]
    course=["B.tech","BBA","PGDM"]
class Student(Ainwik):
        pass
    
obj=Student()
print("<<<<<<Branch>>>>>")
for data in obj.branch:
        print(data)
        print("<<<<<<Course>>>>>")
        for data in obj.course:
            print(data)'''


class A:
    def displayA(self):
        print("Welcome to MyWorld")
class B:
    def displayB(self):
        print("Welcome to My World Zone")   
class c(A,B):
    def displayC(Self):
        print("Welcome to My Home Place")
        
        
obj=c()
obj.displayA()
obj.displayB()
obj.displayC()
    