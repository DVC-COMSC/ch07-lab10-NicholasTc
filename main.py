# ******************************
# Make your Code
# ******************************
numbers = input().split()

# converting ints to strings
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

for j in range(len(numbers)):
    minValue = numbers[j]
    for k in range(j, len(numbers)):
        if minValue > numbers[k]:
            minValue = numbers[k]
    
    # swapping the min and current value
    numbers[numbers.index(minValue)] = numbers[j]
    numbers[j] = minValue

    

    # print()
    # printing the swap progress
    print(numbers)    
