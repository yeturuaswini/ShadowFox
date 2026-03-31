import random

count_6 = 0
count_1 = 0
two_6 = 0
prev = 0

for i in range(20):
    roll = random.randint(1, 6)
    print(roll)

    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if roll == 6 and prev == 6:
        two_6 += 1

    prev = roll

print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Two 6s in a row:", two_6)