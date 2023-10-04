# Lesson on Time Complexity Analysis
def fib(n):
    if n==1:
        return 0
    elif n<=3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Example 1
n = int(input("Enter a number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("No")
        
# Prime Numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 51, 53, 57, 59, 61, 67, 71, 73, 79, 83