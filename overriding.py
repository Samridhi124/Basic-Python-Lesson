class A:
    def showData(self):
        print("I am in class A")
class B(A):
    def showData(self):
        print("In am in B class")
    
obj=B()
obj.showData()