# task5
Students, Count = map(int, input(('Please, insert count of student and subject: ')).split())
marks = []
for subject in range(Count):
    marks += [map(float, input().split())]
for scores in zip(*marks):
    print(sum(scores) / Count)
