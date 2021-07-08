import time

print("=+=+"*10)
print("BEM-VINDO AO SISTEMA DE EMPRÉSTIMOS")
print("=+=+"*10)
print("Por favor, aguarde...")
time.sleep(10)
print("Agora vamos pedir algumas informações.")
salario = float(input('Digite seu salário: R$'))
emprestimo = float(input('Valor do empréstimo desejado: R$'))
anos = int(input('Anos de parcelamento: '))
prestacao = emprestimo / (anos * 12)
portentagem = salario * 30 / 100
print("Estamos analisando sua proposta...")
time.sleep(10)
if portentagem < prestacao :
    print(emoji.emojize("Poxa, neste momento não conseguimos liberar um emprestimo para você "
          " tente novamente daqui alguns meses"))
else:
    print("Parabéns!!!, após nossa analise conseguimos liberar um empréstimo para você")
    print("O valor das parcelas serão R${:.2f}".format(prestacao))