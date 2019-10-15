# Estrutura if - elif - else

x = 1
y = 3
if x < 1:
    print('x menor do que 1')
else:
    print('maior ou igual a 1')

if y > 3:
    print('y é maior do que 3')
elif y==3:
    print('y é igual a 3')
else:
    print('y?? ')
######
# elif pode ser usado mais de uma vez, sendo um intermediario entre o if e o else

# EXEMPLO:

idade = 62
if idade < 12:
    print('criança')
elif idade < 18:
    print('adolescente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')
