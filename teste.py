valores = ['Honda', 'Citroen', 'Peugeot', 'Ferrari', 'Koenigsegg', 'BMW']

carro_pedido = input('Qual é o carro desejado?')

if(carro_pedido in valores):
    print ('Sim, temos o carro')
else:
    print('Não temos o carro')