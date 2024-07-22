import random
import time
from functions import *
from mathgames import *
import os
os.system("cls")
name = input("Enter your name:")
age = input("Enter your age:")
name1 = bool(name)
age1 = bool(age)
name3 = name.replace(" ", "A")
name2 = name3.isalpha()
age2 = age.isdigit()

if name1 == False or age1 == False:
    while True:
        print("You have not completed the submission\nPlease try again:\n....")
        time.sleep(0.5)
        os.system("cls")
        name = input("Enter your name:")
        age = input("Enter Your age:")
        name1 = bool(name)
        age1 = bool(age)
        name3 = name.replace(" ", "A")
        name2 = name3.isalpha()
        age2 = age.isdigit()
        
        if name1 == False or age1 == False:
            continue
        else:
            if name2 == False or age2 == False:
                    print("Your name should be in aphabet form and your age in digit form.\nplease Try again.\n.....")
                    time.sleep(0.5)
                    os.system("cls")
                    continue                     
            else:
                print(f"------------------------------------------------------WELCOME {name.upper()}------------------------------------------------------")
                age = int(age)
                if age <= 18 and age >= 10:
                    function1()
                    break
                elif age <= 8 and age >= 5:
                    function2()
                    break
                elif age > 30:
                    print("Sorry but your are too mature for this game the age limit is from 5 years to 25 years")
                    exit()
                else:
                    print("Invalid age! Please Try again:")
                    continue
else:
    if name2 == False or age2 == False:
            print("Your name should be in aphabet form and your age in digit form.\nplease Try again.\n......")
            time.sleep(0.5)
            os.system("cls")
            name = input("Enter your name:")
            age = input("Enter your age:")
            name1 = bool(name)
            age1 = bool(age)
            name3 = name.replace(" ", "A")
            name2 = name3.isalpha()
            age2 = age.isdigit()
            
            if name1 == False or age1 == False:
                authentication()
    else:
        print(f"------------------------------------------------------WELCOME {name.upper()}------------------------------------------------------")
        age = int(age)
        if age <= 18 and age >= 10:
            function1()
        elif age <= 8 and age >= 5:
            function2()
        elif age > 30:
            print("Sorry but your are too mature for this game the age limit is from 5 years to 25 years")
            exit()
        else:
            print("Invalid age! Please Try again:\n.....")
            time.sleep(0.5)
            os.system("cls")
            authentication()           