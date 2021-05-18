import random

with open("./numbers.txt",mode="w",encoding="utf8") as fout:
    summa=0
    for i in range(200):
        num = random.randint(0,200)
        fout.write(str(num)+" ")
        summa+=num
    
    average=summa/200
    print("Средение:",average)