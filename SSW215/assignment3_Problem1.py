# "I pledge my honor that I have abided by the Stevens Honor System." -Joseph Stefanoni IV
# 10/3/23
# Assignment #3 Problem 1:
f = open("Median.txt", 'r') # If file does not exist, it is created. Previous data is erased when opened.
l = list()
for line in f:
    line = line.strip()
    l.append(int(line))
size = len(l)
l.sort()
if (size == 1):
    median = l[0]
elif (size%2==1):
    median = l[int(size/2)]
else:
    median = (l[int(size/2)] + l[int(size/2-1)])/2
print("The median is:", median)
f.close()
