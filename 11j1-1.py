total = 0
counter = 1
while counter <= 10:
    grade = int(input("Enter grade: "))
    total = grade + total 
    counter = counter + 1
    print(counter)
average = total / 10 
print(average)