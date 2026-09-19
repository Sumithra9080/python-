Data Type	Symbol	                        Main Feature
List	                 []	                         Ordered, changeable
Tuple                   	 ()	                         Ordered, not changeable
Set	                {}	                        Unordered, no duplicates
Dictionary	{key: value}	        Key-value pairs




#data types list[]
'''a=[10,20,30,40,50]
print(a)
print(type(a))
print(a[4])
a.append(60)
print(a)
print(a.count(40))
print(a.index(40))
a.extend([70,80,90,100])
print(a)
print(a.reverse())
print(a)
print(a.pop())
print(a)
print(a.__len__())'''
#trupes() data types
'''a=(10,20,30,40,50)
print(a.index(40))
print(a.count(40))'''
#data types set{}
'''a1={1,2,3,4,5}
a2={5,6,7,8,9,10}
print(a1.union(a2))
print(a1.difference(a2))
print(a1.symmetric_difference(a2))
print(a1.intersection(a2))'''
#disctionary
'''def student():
    data={"name":"sumithra","age":20,"branch":"AI&DS"}
    print(data)
student()'''
#list
'''name = {"sumithra"}
age = {20}
gender = {"male"}
    print(name, age, gender)'''
#dict
'''a={"name":["sumithra","sunl","subash"],
   "age":[20,19,18],
   "gender":["female","male","male"]}
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
a.update({"phone":9080148939})
print(a)
print(a.popitem())
print(a)
new=a.copy()
print(new)
a.clear()
print(a)'''
