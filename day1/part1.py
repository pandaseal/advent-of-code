# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

maxsum = 0
sum = 0

with open('input.txt') as f:
    for line in f:
        calories = line.strip()
        if not len(calories) == 0:
            sum += int(calories)
        else:
            if sum > maxsum:
                maxsum = sum
            sum = 0

# check the last elf
if sum > maxsum:
    maxsum = sum

print(maxsum)