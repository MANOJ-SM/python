
file = open("data.txt","r")

total = 0

for line in file:
    total += int(line) # coverts line into int  and adds them line by line 

file.close()
print("the sum of the numbers is :",total);
