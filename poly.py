'''l=[1,2,3,4,5]
print(len(l))
s="hello guys chai pii lo"
print(len(s))

class Ws:
    def displayinfo(self,name=''):
        print("heloo guyyss"+name)
        
        
obj=Ws()
obj.displayinfo()
obj.displayinfo('python')'''

class Ws:
    def displayinfo(self):
        print("Welcome to Wscubetech")
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to IIP")
        
obj=IIP()
obj.displayinfo()