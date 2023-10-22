import os
import random
from threading import Thread

count1 = 0
count2 = 0

def pr():
    B=True
    while B:
        if count1==10000000-1:
            B=False
       # os.system('cls' if os.name == 'nt' else 'clear')
        print("Поток 2--", count2 * 100 / 2000000, "%  ", "Поток 1--", count1 * 100 / 10000000, "% ")

def increase2(by):
    global count2 
    for i in range(by):
        count2 = i
        counter = random.randint(0, 100)

def increase1(by):
    global count1  
    for i in range(by):
        count1 = i
        counter = random.randint(0, 100)

t1 = Thread(target=increase1, args=(10000000,))
t2 = Thread(target=increase2, args=(2000000,))
t3 = Thread(target=pr)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
