from fractions import Fraction

print('Vamos calcular o problema das torneiras.')
print('Digite os valores de x e y em horas.')
print('Teremos que um determinado volume é preenchido em x horas e outro em y horas,\nem quanto tempo será ambas simultaneamente?')
x = int(input('Digite o valor de x:'))
y = int(input('Digite o valor de y:'))

counter = 0

while x <= 0 or y <= 0:
    print('Digite apenas valores maiores que 0.')
    counter += 1
    x = int(input('Digite o valor de x:'))
    y = int(input('Digite o valor de y:'))

    if counter == 4 or counter == 9:
        print('Teimoso(a) você!')

vazao = (x * y) / (x + y)
decimal = vazao

parseFloat = int(input('Digite quantas casas decimais o resultado deverá ter (máximo 16):\n Digite "20" para resultado exato.'))

if parseFloat == 20:
    fracao = Fraction(decimal).limit_denominator()

if parseFloat == 0:
    decimal = int(vazao)

decimal = round(decimal, parseFloat)

print(f'\n\nTemos que um determinado volume V é preenchido em {fracao} horas.\nEm decimal podemos representar como {decimal} horas.')