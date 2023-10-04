"""
# Lists and for loops
for number in range(20):
    if number%2==0:
        print(number)
     
# Same as before but accepts input.
lb = int(input("Enter lower bound: "))
ub = int(input("Enter upper bound: "))
for number in range(lb, ub+1):
    if number%2==1:
        print(number)
# first = [1, 2, 3, 4]
# len(first) = 4
# first [2:4] = [3, 4
# first + [5, 6] = [1, 2, 3, 4, 5, 6]
# You can concatenate lists with +

first = [1, 2, 3, 4]
first + [5, 6]
second = list(range(1, 5))  # = [1, 2, 3, 4]
print(first==second)
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b = [1, 2, 3, 4, 5, 6]
# [0]*4 = [0, 0, 0, 0]
# [1, 2, 3]*3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# Slices also works on lists

test = list(range(1, 7))
print(test)
print("7 is in list:", 7 in test)
numbers = [2, 3, 4, 5]
print(numbers)
index = 0
while index < len(numbers):
    numbers[index] = numbers[index]**2
    index += 1
# for index in range(len(numbers)):
#     numbers[index] = numbers[index]**2
print(numbers)

# Sentence splitting and uppercase
sentence = "This homework has five questions."
words = sentence.split()
print(words)
for index in range(len(words)):
    words[index] = words[index].upper()
print(words)

example = [1, 2]
print(example)
example.insert(1, 10)
print(example)
example.insert(3, 25)   # Any position greater than the last index will auto assign to the last index.
print(example)
example.extend([11, 12, 13])
print(example)

# List method: append
time_set = []
time_span = 7
for t in range(1, time_span+1):
    time_set.append(t)
print(time_set)
print(len(time_set))

node_set = []
node_num = 5
for i in range(1, node_num+1):
    node_set.append('n%s' % i)  # n is a string, %s is for strings
print(node_set)

# example.pop() removes that last element
# example.pop(0) removes the first element
mylist = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
mylist.remove('Bob')
print(mylist)
# If two names match, it only removes the first one.

# Searching a list
aList = [34, 45, 67]
target = 45
if target in aList:
    print(aList.index(target))
else:
    print(-1)
if 0 not in aList:
    print(aList)

# Sorting a list:
    example.sort() # Sorts numbers in ascending order

Test = [1, 4, 3, 10, 2]
Test.sort()
print("Min:", Test[0], ". Max:", Test[-1])

Test.sort(reverse=True) # Sorts list in descending order

alist = [1, 3, 2, 5]
print(alist.sort()) # Prints None

# A tuple is a type of sequence that resembles a list except it is immutable.
"""
# Example 1:
mylist = [1, -2, 5, 6, 0, 5, 0, 3]
print(mylist)
newList = mylist
while 0 in newList:
    newList.remove(0)
print(newList)
# can also use an if statement and append to a blank list.
