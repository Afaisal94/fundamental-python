print('Tipe data skalar / Tipe data sederhana')

shape1 = 'Square'
shape2 = 'Triangle'
shape3 = 'Circle'

print(shape1)
print(shape2)
print(shape3)

# tipe data list / daftar / array
print('\nTipe data List / Daftar / Array')
# shape = []
# shape.append('Square')
# shape.append('Triangle')
# shape.append('Circle')

shape = ['Square', 'Triangle', 'Circle']
print(shape)
shape.append('Hexagon')
print(shape)

print('\nGet Shape')
print(f'I will using {shape[1]}')

print('\nUsing all shape')
for s in shape:
    print(s)