# task5
r1 = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')
r2 = ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')
r3 = ('z', 'x', 'c', 'b', 'n', 'm')


words = str(input("please insert the word: "))
w1 = words
words = set(words)
rows = ()

if words.intersection(r1) and words.intersection(r2) or words.intersection(r1) and words.intersection(r3):
    print ('Error: litters in word are from different rows')
elif words.intersection(r2) and words.intersection(r3):
    print ('Error: litters in word are from different rows')
else:
    print(w1)
