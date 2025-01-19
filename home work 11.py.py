x=[1,"ahmed",3,7,9,'m',4.1,'h',8]
n=0
y=len(x)
for i in range (len(x)):
    if isinstance(x[i],float):
        n=n+x[i]
    elif isinstance(x[i],int):    
        n=n+x[i]
    else:
        print(f"this is not a number:{x[i]}")  
print(f"the sum is :{n}")          