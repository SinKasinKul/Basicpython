def printName():
    name = "Kasin"
    lastName = 'Kuljiang'
    vRow = 9
    for i in range(vRow):
        #if i == 3: break
        print(name + ' ' + lastName)
    else:
      print("*****END*****")

def testWhile(v):
    while v > 0:
        print(f"Test {v}")
        v -= 1

squares = [x//2 for x in range(0, 11)]
print(squares)

testWhile(98)
