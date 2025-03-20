# While1.py

money = 1000
transfer = 80000

print(money < transfer)

while money < transfer:
    print('Please check your balance.')
    transfer = int(input('New transfer: '))
    if transfer > 10000:
        print("Call Bank Mgr.")
        break
    

print('Transfered.')
