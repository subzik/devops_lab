# task3
F = {'Nik', 'John', 'Tom', 'Bob', 'Den', 'Poul', 'Anna'}
MF = {'Nik', 'Den', 'Mary', 'Nil'}
AFO = set(MF.difference(F))

print('My friends:', " ".join(str(x) for x in F))
print('Mutual Friends:', " ".join(str(y) for y in (MF.intersection(F))))
print('Also Friend of: ', " ".join(str(z) for z in AFO))
