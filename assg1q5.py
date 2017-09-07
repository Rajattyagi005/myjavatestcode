


def max(num1,num2):
    if num1>num2:
        return num1
    if num1<num2:
        return num2
    else:
        return ("Both are equal")


        
num1=int(input("Enter a number :"))
num2=int(input("Enter second number :"))
largest=max(num1,num2)
print(largest)
