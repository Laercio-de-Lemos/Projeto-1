real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.24
print('Com R${:.0f} você pode comprar US${:.0f}'.format(real, dolar))