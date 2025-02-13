import math

max_number = int(input('Find Prime Numbers up to: '))
numbers = list(range(2, max_number))
max_multi = math.floor(math.sqrt(max_number))

for i in numbers:
    if i > max_multi:
        continue
    else:
        for j in numbers[:]:
            if j % i == 0 and j != i:
                numbers.remove(j)

print(numbers)