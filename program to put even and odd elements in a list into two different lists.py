program to put even and odd elements in a list into two different lists
l=[]
even=[]
odd=[]
s=int(input("enter size of list")) 
for i in range(s):
    x=int(input("enter list items"))  
    l.append(x)
for i in range(s):
    if(l[i]%2==0):   
        even.append(l[i])
    elif(l[i]%2!=0):
        odd.append(l[i])
print("even list",even)
print("odd list",odd)