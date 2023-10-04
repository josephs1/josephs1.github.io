# Reading and Writing Files
# Part 1:
total = 0
number = int(input("Enter a number: "))
# add numbers until number is zero
while number != 0:
    total += number     # total = total + number
    # take integer input again
    number = int(input("Enter a number: "))
print("total =", total)

# Part 2:
sum = 0
while True:
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        print("Number is not entered")
        print("The sum is:", sum)
        break
    number = float(data)
    sum += number
    print("The sum is:", sum)

# Example 2:
km = float(input("Enter the number of kilometers: ")) 
mi = km/1.609
print("The number of miles is:", mi)

# Example 3:
num = int(input("Enter a number: "))
for i in range(1, 11):
    print (num, 'x', i, '=', num*i)

# Example 4:
num = int(input("Enter a number: "))
factorial = 1;
if (num<0):
    print("Factorial does not exist for negative numbers.")
elif (num == 0):
    print("The factorial of 0 is 1.")
else:
    for i in range(2, num+1):
        factorial *= i
    print("The factorial of", num, "is:", factorial)

import random

for roll in range(10):
    print(random.randint(1, 6))

# Rolling two dice
r1 = random.randint(1,6)
r2 = random.randint(1,6)
total = r1+r2
print("You rolled", r1, "and", r2, "for a total of:", total)
if (total>6):
    print("Good job! The total was greater than 6.")

# Guesser game
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNum = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNum = int(input("Enter your guess: "))
    if userNum < myNum:
        print("Too small!")
    elif userNum > myNum:
        print("Too large!")
    else:
        print("Congratulations! You got it in", count, "tries!")
        break

# len("Hi there!") # Prints out the length of the strength
# Prints out the index of each character along with the character at that position.
data = "Hi there!"
for index in range(len(data)):
    print(index, data[index])
    
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for i in fileList:
    if ".txt" in i:
        print(i)

#substrings:
    # name [0:2] # First two characters
    # name [:len (name)] # The entire string
    # name [-3:] # The last 3 characters

"myfile.txt".split ('.') # prints: ['myfile', 'txt']

# Opening and writing files:
f = open("Test.txt", 'w') # If file does not exist, it is created. Previous data is erased when opened.
f.write("First line.\nSecondline.\n")
f.close()

# line = f.readline()
# line = line.strip()

# Writing numbers to a file:
f = open("integers.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")
f.close()

 f = open ("Test.txt", 'r') # Reads from a file
 for line in f:
     print(line)
  
f = open ("integers.txt", 'r')
sum = 0
for line in f:
    line = line.strip ()
    number = int (line)
    sum += number
print ("The sum is", sum)