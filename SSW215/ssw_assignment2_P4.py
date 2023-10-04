# Joseph Stefanoni
# "I pledge my honor that I have abided by the Stevens Honor System." -Joseph Stefanoni
# Problem 4:
lower = int(input("Enter the lower bounds: "))
upper = int(input("Enter the upper bounds: "))
for i in range(lower, upper+1):
    if i%2==1:
        print(i)