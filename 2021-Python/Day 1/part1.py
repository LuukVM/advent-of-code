file = open("Day 1/values.txt", "r")

values = file.read().splitlines()

previousValue = 0
increases = 0


for x in range(len(values)):
    if int(values[x]) > previousValue and x != 0:
        increases = increases + 1
    previousValue = int(values[x])

print(increases)

file.close()
