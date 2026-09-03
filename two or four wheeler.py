V = int(input("no.of vehicles: "))
W = int(input("no.of wheels: "))

if W < 2 or W % 2 != 0 or V >= W:
    print("INVALID INPUT")
else:
    FW = (W - 2 * V) // 2
    TW = V - FW

    if TW < 0 or FW < 0:
        print("INVALID INPUT")
    else:
        print("TW =", TW, "FW =", FW)