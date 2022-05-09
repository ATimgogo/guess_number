import random
start = input("請輸入最小值:")
end = input("請輸入最大值:")
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    count += 1 #count = count + 1的快寫法
    g = input("請猜一個數字:")
    g = int(g)
    if g == r:
        print("恭喜答對!")
        print("您猜了", count,"次")
        break
    elif g > r:
        print("比答案大")
    elif g < r:
        print("比答案小")
    print("您猜錯了", count,"次")