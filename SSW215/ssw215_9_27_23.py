# Lesson on Dictionaries
"""
info = {} # Creating an empty dictionary
info ["name"] = "Sandy" # Adding a key and value pair to a dictionary
info ["occupation"] = "hacker"
print(info)
info ["occupation"] = "manager" # Replacing a value with an existing key in a dictionary
info ["name"] = "Alice"
print(info)

grades = {'John':'A','Emily':'A+', 'Betty':'B', 'Mike':'C'}
grades_new = {'John':'B', 'Sam':'A', 'Betty':'A'}
grades.update(grades_new) # Updating a list with another list. Replaces or adds where necessary.
print(grades)

grades2 = {'John':'A', 'Mike':'B', 'Emily':'C'}
for i in grades2:
    print(i) # Prints the names

my_info = {'name':'Sandy','occupation':'manager', 'age': '38'}
theKeys = list (my_info.keys ())
theKeys.sort()
print(theKeys)
for key in theKeys:
    print(key, my_info[key])

# Example 1:
data = {}
for i in range(1, 16):
    data [i] = i**2
print(data)

# Example 2: Multiply all numbers in a dictionary together.
info = {'n1':1, 'n2':2, 'n3':3, 'n4':4, 'n5':7}
result = 1
for key in info:
    result *= info[key]
print(result)

# Example 3:
data = {'n1':1, 'n2':2, 'n3':3, 'n4':4, 'n5':7}
print(sum(data.values()))
# Can also do:
total = 0
for i in data:
    total += data[i]
print(total)

# Example 4:
import random
workers = {}
while True:
    gen = input("Enter a worker's name or nothing to exit: ")
    if (gen == ""):
        sorted_workers = sorted(workers.items(), key=lambda x: x[1]) # [1] for values, [0] for keys
        print(sorted_workers)
        break
    else:
        salary = random.randint(5000, 10000)
        workers [gen] = salary

# Example 5:
ints = [1, 2, 3, 1, 4, 12, 4, 2, 4, 4, 1]
no_dup = []
dup = []
for i in ints:
    if i not in no_dup:
        no_dup.append(i)
    elif i not in dup:
        dup.append(i)
print ("Duplicate list: ", dup)
"""
import random
for i in range(15):
    r1 = random.randint(1, 6)
    print(r1)