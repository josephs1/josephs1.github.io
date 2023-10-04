# Joseph Stefanoni
# "I pledge my honor that I have abided by the Stevens Honor System." -Joseph Stefanoni
# Problem 3:
total = 0
avg = 0.0
count = 0;
while True:
    num = input("Enter numbers or press enter to stop: ")
    if num == "":
        avg = total/count
        print("The sum is: ", total)
        print("The average is: ", avg)
        break
    else:
        total += float(num)
        count += 1