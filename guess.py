from random import randint
secret = randint(1,99)
guess=0
tries=0
print("AHOY! I'm the Dread Pirate Roberts,and I have a secert!")
print("It is a number from 1 to 99.I'll give you 6 tries.")
while guess !=secret and tries <6:
    guess =int (input("What's yer guess?")) #input 返回类型是str类型，不能直接和整数进行比较，使用int()方法
    if guess < secret:
        print("Too low,ye scurvy dog！")
    elif guess > secret:
        print("Too high,landlubber!")
    tries = tries+1  
if guess == secret:  #注意空格位置，如果与上一行同行，无法执行tries
        print("Avast! Ye got it! Found my secret,ye did!")
else:
        print("No more guesses! Better luck next time,matey!")
        print("The secert number was",secret)
