# "I pledge my honor that I have abided by the Stevens Honor System." -Joseph Stefanoni IV
# 10/3/23
# Assignment #3 Problem 3:
primes = list()
nonprimes = list()
for i in range(1, 101):
    flag = True
    for count in range(i-1, 1, -1):
        if i%count==0:
            flag = False
            break
    if flag and i!=1:
        primes.append(i)
    else:
        nonprimes.append(i)
print("Prime numbers from 1-100:", primes)
print("Non-prime numbers from 1-100:", nonprimes)
    
