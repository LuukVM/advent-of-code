file = open("2021-Python/Day 2/values.txt", "r")
# file = open("2021-Python/Day 2/sample.txt", "r")

values = file.read().split()

horizontalPosition = 0
verticalPosition = 0
aim = 0

for x in range(len(values)):
    if values[x] == "forward":
        horizontalPosition += int(values[x + 1])
        verticalPosition += int(values[x + 1]) * aim
    elif values[x] == "up":
        aim -= int(values[x + 1])
    elif values[x] == "down":
        aim += int(values[x + 1])

print(horizontalPosition * verticalPosition)

