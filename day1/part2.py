# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

topthree = []
elfsum = 0

with open('input.txt') as f:
    for line in f:
        calories = line.strip()
        if not len(calories) == 0:
            elfsum += int(calories)
        else:
            # add the first three without comparison
            # for the rest (else), check if they should be added
            if len(topthree) < 3: 
                topthree.append(elfsum)
            else: 
                lowest = min(topthree)
                if elfsum > lowest:
                    topthree.remove(lowest)
                    topthree.append(elfsum)

            # continue to next
            elfsum = 0

# check the last elf
if len(topthree) < 3: 
    topthree.append(elfsum)
else: 
    lowest = min(topthree)
    if elfsum > lowest:
        topthree.remove(lowest)
        topthree.append(elfsum)


# sum up topthree's calories
sum = 0
for elf in topthree:
    print(elf)
    sum += elf

print(sum)