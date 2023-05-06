import random

print("猜数字游戏")

# 随机生成一个 1~100 的整数
number = random.randint(1, 100)

# 循环猜测
while True:
    guess = int(input("请输入一个 1~100 的整数："))

    if guess == number:
        print("恭喜你，猜对了！")
        break
    elif guess > number:
        print("猜大了，请再猜一次。")
    else:
        print("猜小了，请再猜一次。")
