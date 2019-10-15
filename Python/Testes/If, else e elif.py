x = 4
y = 9
z = 16

if (x+y < z):
    print('(x+y)' + '(' + str(x+y) + ')' + 'é menor que: ' + str(z)+', que é z')
else:
    print('x+y é maior que z')
############################################

if (z-x > y):
    print('y é menor que: ' + str(z-x) + ', que é (z-x)')
else:
    print('y é maior que: (z-x)')

#############################################

if (x+y+z < 20):
    print('A soma destes três itens (x+y+z) não ultrapassa 20')
else:
    print('A soma destes três itens (x+y+z) ultrapassa 20, sendo ela: ' + str(x+y+z))
