file = open("Day 1/values.txt", "r")

values = file.read().splitlines()

values = list(map(int, values))

increases = 0

for x in range(len(values) - 3):
    if values[x] + values[x + 1] + values[x + 2] < values[x + 1] + values[x + 2]+ values[x + 3]:
        increases += 1

print(increases)

file.close