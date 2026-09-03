#coin exchange
amount=int(input("Enter amount:"))
coins=[500,200,100,50,20,10,5,2,1]
print("Coins used: ")
tc=0
for coin in coins:
    while amount>=coin:
        count=amount//coin
        print(f"{coin}X{count}")
        amount=amount%coin
        tc+=count
print("Total coins used: ",tc)


