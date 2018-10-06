temp = 25
wait = 60

if temp < 20:
    print("Eat soup!")
    print("Enjoy!")
    if wait >= 40:
        print("Order a delivery")
    else:
        print("Prepare dinner yourself")
else:
    print("Eat a salad!")
print("Bon appetit!")