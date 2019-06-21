# task4
testlist = input("Please, enter few numbers: ").split()
testlist2 = list(map(int, testlist))
pozsum = 0


for i in range(len(testlist)):
    if testlist[i] > '0':
        temp = int(testlist[int(i)])
        pozsum += temp
    print()
min_id = testlist2.index(min(testlist2))
max_id = testlist2.index(max(testlist2))

m = 1
for i in range(min_id + 1, max_id):
    m *= testlist2[i]
print('Sum of numbers is:', pozsum,
      '\nMultiple of numbers, \n'
      'which stay between \n'
      'biggest and smallest numbers is:', m)
