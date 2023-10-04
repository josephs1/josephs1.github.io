# "I pledge my honor that I have abided by the Stevens Honor System." -Joseph Stefanoni IV
# 10/3/23
# Assignment #3 Problem 2:
l = list()
while True:
    data = input("Enter an integer to add to a list or nothing to stop: ")
    if (data == ""):
        break
    else:
        l.append(int(data))
rl = list()
for i in range(len(l)-1, -1, -1):
    rl.append(l[i])
print("Original List:", l)
print("Reversed List:", rl)
    
        