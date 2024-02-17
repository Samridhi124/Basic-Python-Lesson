'''data="Hello Everyone"
print (data[6])
print (data[-1])
print (data[9])
print (data[-7]) indexing'''

''' string slicing school="hello gd mrng"
print (school[5: ])
print(school[:5])
print(school[-5:-3])'''


#string iteration
'''x="Welcome to School"
y=len(x)
print(y)
for a in range(y):
    print (x[a])
    
    print(" ")
for a in range(y-1,-1,-1):
        print(x[a])
w="welcome guys"   
for a in w:
            print (a)'''
            
            #string fn
            #upper,lower,title,capitalize,index,find,isalpga,isdigit,isalnum

'''a="Welcome Friends to Party"
n=a.lower()
print(n)

b=a.upper()
print(b)

c=a.title()
print(c)

d=a.capitalize()
print(d)
a="Welcome"
print(a.index('o',3))

w="Welcome"
x="1233"
y="wleocme2234"
z="900"
print(z.isalpha())
print(w.isalpha())
print(x.isdigit())
print(y.isalnum())

#chr() and ord()

a=68;
print(chr(a)); 

y='A'
print(ord(y));'''
#format()
a="Welcome {} to {} College ".format("Hello",20)
print(a)

a="Welcome {0} to {1} College ".format("Hello",20)
print(a)

x="Welcome {b:10} to {a:20} College ".format(a=10,b=20)
print(x)
