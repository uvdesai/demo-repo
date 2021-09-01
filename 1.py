"""
*
**
***
****
*****
i=1,j=1 to 5 
rows=5
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print(' ')

  


    for j in range(rows,i-1):
        print("*",end=" ")

    print(" ")

  

  rows=5
for i in range(1,rows+1):
    for j in range(1,(rows-i)+1):
        print(" ",end="")
    
    for k in range(1,i+1):
        print("*",end="")
    print(" ")


    rows=5
for i in range(1,rows+1):
    for j in range(1,(rows-i)+1):
        print(" ",end="")
    
    for k in range(1,i+1):
        print("* ",end="")
    print(" ")
# 
rows=5
for i in range(1,rows+1):
    for k in range(1,rows+1):
        print(" *",end="")
    rows-=1
    print(" ")


  """



# right start pattern of star
rows=5
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print(' ')
for i in range(rows):
    for k in range(rows-1):
        print("*",end=" ")
    rows-=1
    print(' ')

