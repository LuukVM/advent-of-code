# file = open("2021-Python\Day 3\sample.txt", "r")
file = open("2021-Python/Day 3/values.txt", "r")

values = file.read().splitlines()

def calculateValues(reverse, bits):
    for x in range(len(bits[0])):
        zeros = []
        ones = []
        for y in range(len(bits)):
            if int(bits[y][x]) == 0:
                zeros.append(bits[y])
            else: 
                ones.append(bits[y])
        if len(zeros) > len(ones):
            bits = zeros if reverse else ones
        elif len(zeros) == len(ones):
            bits = ones if reverse else zeros
        else:
            bits = ones if reverse else zeros

        if len(bits) == 1:
            return bits


generatorBits = calculateValues(False, values)
scrubberBits = calculateValues(True, values)
generator = 0
scrubber = 0

for bit in generatorBits[0]:
    generator = (generator << 1) | int(bit)

for bit in scrubberBits[0]:
    scrubber = (scrubber << 1) | int(bit)
    

print(scrubber * generator)
