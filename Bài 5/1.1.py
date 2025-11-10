import mymath
list = [2,3,4,5]
print('Square:')
for v in list:
     m = mymath.square(v)
     print(m, end=' ')

print('\nCube:')
for v in list:
    print(mymath.cube(v))

print('\nValues:'+ str(mymath.average(list)))


