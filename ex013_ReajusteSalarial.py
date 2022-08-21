salario = float(input('Qual é o salário do funcionário? R$'))
novo_salario = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo_salario))

# Exemplo
emprestimo = float(input('Quanto peguei emprestado?'))
emprestimo_pago = emprestimo + (emprestimo * 10 / 100)
print('O valor que peguei emprestado é R${:.2f}, ao final, vou pagar R${:.2f}'.format(emprestimo, emprestimo_pago))
