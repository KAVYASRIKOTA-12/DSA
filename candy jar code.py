N = 10
K = 5

candies = N

order = int(input("Candies ordered: "))

if order <= 0:
    print("INVALID INPUT")
    print("NUMBER OF CANDIES LEFT :", candies)

elif order > candies:
    print("INVALID INPUT")
    print("NUMBER OF CANDIES LEFT :", candies)

else:
    candies -= order

    print("NUMBER OF CANDIES SOLD :", order)

    if candies <= K:
        candies = N

    print("NUMBER OF CANDIES LEFT :", candies)