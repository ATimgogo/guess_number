import random
r = random.randint(1, 100)
while True:
    g = input("請猜一個數字:")
    g = int(g)
    if g == r:
        print("恭喜答對!")
        break
    elif g > r:
        print("比答案大")
    elif g < r:
        print("比答案小")