print('Welcome to bank <name of bank>')
salario = float(input('Please enter your current salary: $'))
casa = float(input('Please now enter the value of the property you wish to purchase with the loan: $'))
tempo = int(input('How long do you intend to pay off the loan in years? '))
valMax = salario * 30/100
temparcela = tempo * 12
parcela = casa / temparcela
if parcela <= valMax:
    print('Your loan has been approved! Here is a summary of the negotiation:')
    print('Total value of the property: ${} '.format(casa))
    print('Number of installments and value: {}x of ${:.2f}'.format(temparcela, parcela))
else:
    print('Unfortunately, we will not be able to authorize your loan to purchase this property, we are very sorry.')
