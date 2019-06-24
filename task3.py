# task3
F = {'Nik', 'John', 'Tom', 'Bob', 'Den', 'Poul', 'Anna'}
MF = {'Nik', 'Den', 'Mary', 'Nil'}
AFO = set(MF.difference(F))

print('My friends:', " ".join(x for x in F))
print('Mutual Friends:', " ".join(y for y in (MF.intersection(F))))
print('Also Friend of: ', " ".join(z for z in AFO))
