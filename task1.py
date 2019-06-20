# task1
scores = []

num = int(input("How many scores you wont to enter?: "))

for i in range(1, num + 1):
    sc = int(input("Enter scores: "))
    scores.append(sc)

scores.sort()

print("Second place score from list is:", scores[-2])
