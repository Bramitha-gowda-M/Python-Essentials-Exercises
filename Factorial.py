num = int(input("Enter the number : "))

num1 = 1

# Approach 1 : Using loops
if num <=0 :
    print("There is no factorial number for negative number")
elif num == 0:
    print("The factorial of 0 is 1")   
else:
    for i in range(1,num+1):
        num1 = num1 * i
        
    print(f"Factorial of {num} is {num1}")
    
    
#Approach 2 : Using Recursive method
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    #or
    return 1 if(n==1 or n==0) else n*fact(n-1)

num = 6

print(f"The factorial of {num} is {fact(num)}")    