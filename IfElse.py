# ifelse.py

money = 5

if money >= 300:
    print(f'You are can go dinner Jpan style with money {money}')
elif money >= 50 or money <= 100:
    print('Go thai style.')
elif money == 0 or money <= 50:
    print('Go to work now!!!.')
else :
    print('Sleep at home.') 


friend = ['Kai','Tew','Keaw']
friend2 = {
            'Tew': 'Mr.'
           }
vistor = 'Tew'

def CheckFriend(V):
    V = V.title() 
    if V in friend or V.title() in friend:
        print(f"{V} is my friend.")
        if V in friend2 or V.title() in friend2:
            print(f'Hi {friend2[V]}{V} welcome.')
        else:
            print(f'Hi {V}, Now,I bussy')
    else:
        print(f"{V} is Not my friend.")
    print(f"List friend is {friend}.")

CheckFriend(vistor)