#Iterative Control Flow in Python
for loop
while loop


#Print 1 to 5

for i in range(1, 6):
    print(i)


#for Loop

    for i in range(5):
    print("Hello")

##Print Even Numbers

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
##Print Odd Numbers

for i in range(1, 11):
    if i % 2 != 0:
        print(i)

##while Loop
i = 1

while i <= 5:
    print(i)
    i = i + 1


##While Loop – Even Numbers
i = 2

while i <= 10:
    print(i)
    i = i + 2


##Loop with if Condition
for i in range(1, 11):

    if i == 5:
        print("Five")

    else:
        print(i)





for → repeats
if → checks condition
else → executes when condition is false






#for condition
'''for i in range(5,0,-1):
    print(i)'''
#for break condition
'''for i in range(5):
    if i==3:
        break
    print(i)'''
#for nested loop
'''for i in range(2):
    for j in range(3):
        print(i,j)'''
#string for loop
'''a="python"
for i in a:
    print(i)'''
#end function for loop
'''a="karthi sumi"
for i in a:
    print(i,end=" ")'''
'''for i in range(1,51,3):
    print(i)'''
#while loop incriment
'''i=1
while i<=5:
    print(i)
    i+=1'''
#while loop dcri
'''i=5
while i>=1:
    print(i)
    i-=1'''
#print 1 to 10 numbers
'''num=1
while num<=10:
    print(num)
    num+=1'''
#even number
'''k=2
while k<=20:
    print(k)
    k+=2'''
#revers
'''num=1234
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)'''
#palandrum
'''a=121
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)'''
#spy number
'''a=123
b=0
c=1
t=a
while t>0:
    d=t%10
    b=b+d
    c=c*d
    t=t//10
print(b)'''
#armstrong number
'''a=153
b=0
t=a
while t>0:
    d=t%10
    b+=d**3
    t=t//10
print(b)'''
#fibonacci
'''a=10
b=0
t=1
count=0
while count<a:
    print(b)
    c=b+t
    b=t
    t=c
    count+=1'''

