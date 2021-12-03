# file = open("2021-Python\Day 3\sample.txt", "r")
file = open("2021-Python/Day 3/values.txt", "r")

values = file.read().splitlines()

gammaBits = []
epsilonBits = []
gamma = 0
epsilon = 0

for x in range(len(values[0])):
    zeros = 0
    ones = 0
    for y in range(len(values)):
        if int(values[y][x]) == 0:
            zeros += 1
        else: 
            ones += 1
    if zeros > ones:
        gammaBits.append(0)
        epsilonBits.append(1)
    else:
        gammaBits.append(1)
        epsilonBits.append(0)

for bit in gammaBits:
    gamma = (gamma << 1) | bit

for bit in epsilonBits:
    epsilon = (epsilon << 1) | bit
    

print(gamma * epsilon)
