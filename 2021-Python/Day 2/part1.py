file = open("2021-Python/Day 2/values.txt", "r")

values = file.read().split()

horizontalPosition = 0
verticalPosition = 0

for x in range(len(values)):
    if values[x] == "forward":
        horizontalPosition += int(values[x + 1])
    elif values[x] == "up":
        verticalPosition -= int(values[x + 1])
    elif values[x] == "down":
        verticalPosition += int(values[x + 1])

print(horizontalPosition * verticalPosition)
