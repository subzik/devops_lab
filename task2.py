# task2
A = int(input("Please insert A from 1 to 32768: "))
B = int(input("Please insert B from 0 to 32768: "))
C = int(input("Please insert C from 0 to 32768: "))
D = int(input("Please insert D from 0 to 32768: "))
root = 0

for x in range(-100,101):
    if 0 == A*x*x*x+B*x*x+C*x+D:
        root=root+1
        print('x', root, '=', x)
if root == 0:
    print ('there no full numbers')