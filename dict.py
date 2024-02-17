'''details={"names":"Aimt","Course":"Python","Duration":"3months"}
print(details)
f=details['names']
print(f)

# 1st way to read items from dict
for key,value in details.items():
    print(key,"\t", value)
    #read keys
    print("List of keys")
    for key in details.keys():
        print(key)
        #read values
        print("List of values")
        for values in details.values():
            print(value)
            '''
            #nested dict
            
course = {
    'php': {'duration': '2 months', 'fees': '9000'},
    'c': {'duration': '2 months', 'fees': '8000'},
    'java': {'duration': '2 months', 'fees': '2000'}
}

print(course)
print['java']['fees']=25000
print(course['php'])

for k,v in course.items():
    print(k,v)
    
