"""
#Write a Python program to find those numbers which are divisible by 3 and multiple
#of 5, between 1000 and 3000 (both included).
for num in range(1000,3000):
    if num % 3 == 0  and num % 5 == 0:

        print(num)

add=0
for i in range(0,10):
    n =int(input("enter the no:"))
    add=add+n
add=add/10
print(add)


 """
 #wrong way
"""
count=0
add=0
n=(input("enter how many no you want to enter"))
for i in n:
    x=input("enter the no")
    
    if(x== 'q' or x== 'Q'):
        break 
    add=add+int(x)
    count=count+1

add=add/count
print(add)
"""


add=0
count=0
while(True):
    num=input("enter the no")
    if(num=='q' or num=='Q'):
        break
    else:
        add=add+int(num)
        count+=1
add=add/count
print(add)



