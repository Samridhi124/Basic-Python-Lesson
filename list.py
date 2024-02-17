
#inserting elements from the list using array[]brackets
'''places=[]
print("Size before adding element is:",len(places))
places=["mana","goa","noida","delhi"]
print("Size after adding element is:",len(places))
places.remove["noida"]
print("Size after removing element is:",len(places))'''
#Read Elements from the lisids=[101,102,103,104]
#list 1st way to record
'''for data in ids:
    print(data)'''
    #2nd way
'''i=0
while i<len(ids):
    print(ids[i])
i=i+5'''
        #3rd way using slicing method
#print(ids[0:3])


#reverse list using loop
'''ids=[1,2,3,4,5]
for i in range (len(ids)-1,-1,-1):
    print(ids[i])'''
    
    #commonly function used in list
'''name=["noida","delhi","goa","patna"]
#1st way to remove
name.remove("noida")
print(name)
#2nd way
name.pop(2)
print(name)
#3rd way
name.clear()
print(name)
#4th way
del name
print(name)'''
#insert records inside list

'''name=["Ram","Shyam"]
#insert value in list using index
name.insert(1,"sita")
print(name)
name.append("Radhe")
print(name)'''

#take an inppput from user and insert records information in list
'''list=[]
print("Enter Records\n")
print("-------------------------------")
for i in range(5):
    value=input()
    list.append(value)
    print("-----------------------")
    print("##########Records###########")
    for i in list:
        print(i)'''
        
        #2nd way to create list using() function
'''name=list(["Sam","RIdhi","Raj"])
print(name)
#merge list 
name=["S","a","m"]
name2=["r","i"]
name.extend(name2)
print(name)
#reverse
l=[1,2,3,4,5]
t=len(l)
for n in range(t-1,-1,-1):
    print(l[n])
for a in len:
        print(a)
        
        
l=[1,2,3,4,5]
t=len(l)     
for a in range(t-1,-1,-1):
        print(l[a])
        
        
        
        #elgant way
        
l=[]
for a in range(1,101):
    l.append(a)
print(l)

n=[m for  m in range(1,101)]
print(n)'''

s="hello"
d=[g for g in s]
print(d)