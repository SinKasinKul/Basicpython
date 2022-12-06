# While1.py

money = 1000
transfer = 80000

print(money < transfer)

while money < transfer:
    print('Please check your balance.')
    transfer = input('New transfer:')

print('Transfered.')