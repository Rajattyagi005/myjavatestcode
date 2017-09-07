base=int(input("Enter the value of Base :"))
exp=int(input("Enter the value of exp :"))
sum=1
i=0
for i in range(1,exp+1):
    sum=sum*base
    
print("Value of exponential :",sum)   
