import json

d='{"cname":"Python","fees":"1000","duration":"2 Months"}'
x=json.loads(d)
print(type(x))
print(x)
for a in x:
    print(a,x[a])