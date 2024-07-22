import random
import time
import os
def function1():
    points = 0
    correct = 0 
    incorrect = 0
    answered = 0
    unanswered = 0 
    levels = 1
    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
    for x in range(11):
        numr = random.randrange(10, 20)
        numl = random.randrange(10, 20)
        Question = input(f"{numl} + {numr} =")
        answer = numl + numr
        Question1 = bool(Question)
        Question2 = Question.isdigit()
        
        if Question1 == False:
            points -= 2
            unanswered += 1
            print("You have not entered the answer to the question\nTherefore you lost 2 points.")
            time.sleep(0.5)
            os.system("cls")
            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
            print(f"Points : {points}")
            if points <= 0:
                print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                print(f"""
                        Answered   :{answered}
                        Unanswered :{unanswered}
                        Correct    :{correct}
                        Incorrect  :{incorrect}
                        Points     :{points}""")
                exit()
            else:
                continue
        else: 
            if Question2 == False:
                points -= 1
                answered += 1
                print("You have to enter your answer as a digit and not a character for that you have lost 1 point")
                time.sleep(0.5)
                os.system("cls")
                print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                print(f"Points : {points}")
                if points <= 0:
                    print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                    print(f"""
                          Answered   :{answered}
                          Unanswered :{unanswered}
                          Correct    :{correct}
                          Incorrect  :{incorrect}
                          Points     :{points}""")
                    exit()
                else:
                    continue
            else:
                Question = int(Question)
                if Question == answer:
                    points += 5
                    answered += 1 
                    correct += 1
                    print("Congrats! you haves scored 5 points")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                else:
                    points -= 5
                    answered += 1
                    incorrect += 1 
                    print("Opps! Worng answer you have lost 5 points")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                    if points <= 0:
                        print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                        print(f"""
                             Answered   :{answered}
                             Unanswered :{unanswered}
                             Correct    :{correct}
                             Incorrect  :{incorrect}
                            Points      :{points}""")
                        exit()
                    else:
                        continue
    if x == 10:
        levels += 1
        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
        for y in range(21):
            numr = random.randrange(20, 30)
            numl = random.randrange(20, 30)
            Question = input(f"{numl} x {numr} =")
            answer = numl * numr
            Question1 = bool(Question)
            Question2 = Question.isdigit()
            
            if Question1 == False:
                points -= 2
                unanswered += 1
                print("You have not entered the answer to the question\nTherefore you lost 2 points.")
                time.sleep(0.5)
                os.system("cls")
                print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                print(f"Points : {points}")
                if points <= 0:
                    print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                    print(f"""
                        Answered   :{answered}
                        Unanswered :{unanswered}
                        Correct    :{correct}
                        Incorrect  :{incorrect}
                        Points     :{points}""")
                    exit()
                else:
                    continue
            else: 
                if Question2 == False:
                    points -= 1
                    answered += 1
                    print("You have to enter your answer as a digit and not a character for that you have lost 1 point")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                    if points <= 0:
                        print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                        print(f"""
                            Answered   :{answered}
                            Unanswered :{unanswered}
                            Correct    :{correct}
                            Incorrect  :{incorrect}
                            Points     :{points}""")
                        exit()
                    else:
                        continue
                else:
                    Question = int(Question)
                    if Question == answer:
                        points += 5
                        answered += 1 
                        correct += 1
                        print("Congrats! you haves scored 5 points")
                        time.sleep(0.5)
                        os.system("cls")
                        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                        print(f"Points : {points}")
                    else:
                        points -= 5
                        answered += 1
                        incorrect += 1 
                        print("Opps! Worng answer you have lost 5 points")
                        time.sleep(0.5)
                        os.system("cls")
                        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                        print(f"Points : {points}")
                        if points <= 0:
                            print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                            print(f"""
                                Answered   :{answered}
                                Unanswered :{unanswered}
                                Correct    :{correct}
                                Incorrect  :{incorrect}
                                Points      :{points}""")
                            exit()
                        else:
                            continue
        if y == 20:
            levels += 1
            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
            for z in range(31):
                numr = random.randrange(30, 40)
                numl = random.randrange(30, 40)
                Question = input(f"{numl} - {numr} =")
                answer = numl - numr
                Question1 = bool(Question)
                Question2 = Question.isdigit()
                
                if Question1 == False:
                    points -= 2
                    unanswered += 1
                    print("You have not entered the answer to the question\nTherefore you lost 2 points.")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                    if points <= 0:
                        print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                        print(f"""
                            Answered   :{answered}
                            Unanswered :{unanswered}
                            Correct    :{correct}
                            Incorrect  :{incorrect}
                            Points     :{points}""")
                        exit()
                    else:
                        continue
                else: 
                    if Question2 == False:
                        points -= 1
                        answered += 1
                        print("You have to enter your answer as a digit and not a character for that you have lost 1 point")
                        time.sleep(0.5)
                        os.system("cls")
                        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                        print(f"Points : {points}")
                        if points <= 0:
                            print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                            print(f"""
                                Answered   :{answered}
                                Unanswered :{unanswered}
                                Correct    :{correct}
                                Incorrect  :{incorrect}
                                Points     :{points}""")
                            exit()
                        else:
                            continue
                    else:
                        Question = int(Question)
                        if Question == answer:
                            points += 5
                            answered += 1 
                            correct += 1
                            print("Congrats! you haves scored 5 points")
                            time.sleep(0.5)
                            os.system("cls")
                            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                            print(f"Points : {points}")
                        else:
                            points -= 5
                            answered += 1
                            incorrect += 1 
                            print("Opps! Worng answer you have lost 5 points")
                            time.sleep(0.5)
                            os.system("cls")
                            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                            print(f"Points : {points}")
                            if points <= 0:
                                print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                                print(f"""
                                    Answered   :{answered}
                                    Unanswered :{unanswered}
                                    Correct    :{correct}
                                    Incorrect  :{incorrect}
                                    Points     :{points}""")
                                exit()
                            else:
                                continue  

def function2():
    points = 0
    correct = 0 
    incorrect = 0
    answered = 0
    unanswered = 0 
    levels = 1
    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
    for x in range(11):
        numr = random.randrange(5, 10)
        numl = random.randrange(5, 10)
        Question = input(f"{numl} + {numr} =")
        answer = numl + numr
        Question1 = bool(Question)
        Question2 = Question.isdigit()
        
        if Question1 == False:
            points -= 2
            unanswered += 1
            print("You have not entered the answer to the question\nTherefore you lost 2 points.")
            time.sleep(0.5)
            os.system("cls")
            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
            print(f"Points : {points}")
            if points <= 0:
                print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                print(f"""
                        Answered   :{answered}
                        Unanswered :{unanswered}
                        Correct    :{correct}
                        Incorrect  :{incorrect}
                        Points     :{points}""")
                exit()
            else:
                continue
        else: 
            if Question2 == False:
                points -= 1
                answered += 1
                print("You have to enter your answer as a digit and not a character for that you have lost 1 point")
                time.sleep(0.5)
                os.system("cls")
                print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                print(f"Points : {points}")
                if points <= 0:
                    print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                    print(f"""
                          Answered   :{answered}
                          Unanswered :{unanswered}
                          Correct    :{correct}
                          Incorrect  :{incorrect}
                          Points     :{points}""")
                    exit()
                else:
                    continue
            else:
                Question = int(Question)
                if Question == answer:
                    points += 5
                    answered += 1 
                    correct += 1
                    print("Congrats! you haves scored 5 points")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                else:
                    points -= 5
                    answered += 1
                    incorrect += 1 
                    print("Opps! Worng answer you have lost 5 points")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                    if points <= 0:
                        print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                        print(f"""
                             Answered   :{answered}
                             Unanswered :{unanswered}
                             Correct    :{correct}
                             Incorrect  :{incorrect}
                            Points      :{points}""")
                        exit()
                    else:
                        continue
    if x == 10:
        levels += 1
        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
        for y in range(21):
            numr = random.randrange(10, 20)
            numl = random.randrange(10, 20)
            Question = input(f"{numl} x {numr} =")
            answer = numl * numr
            Question1 = bool(Question)
            Question2 = Question.isdigit()
            
            if Question1 == False:
                point -= 2
                unanswered += 1
                print("You have not entered the answer to the question\nTherefore you lost 2 points.")
                time.sleep(0.5)
                os.system("cls")
                print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                print(f"Points : {points}")
                if points <= 0:
                    print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                    print(f"""
                        Answered   :{answered}
                        Unanswered :{unanswered}
                        Correct    :{correct}
                        Incorrect  :{incorrect}
                        Points     :{points}""")
                    exit()
                else:
                    continue
            else: 
                if Question2 == False:
                    points -= 1
                    answered += 1
                    print("You have to enter your answer as a digit and not a character for that you have lost 1 point")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                    if points <= 0:
                        print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                        print(f"""
                            Answered   :{answered}
                            Unanswered :{unanswered}
                            Correct    :{correct}
                            Incorrect  :{incorrect}
                            Points     :{points}""")
                        exit()
                    else:
                        continue
                else:
                    Question = int(Question)
                    if Question == answer:
                        points += 5
                        answered += 1 
                        correct += 1
                        print("Congrats! you haves scored 5 points")
                        time.sleep(0.5)
                        os.system("cls")
                        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                        print(f"Points : {points}")
                    else:
                        points -= 5
                        answered += 1
                        incorrect += 1 
                        print("Opps! Worng answer you have lost 5 points")
                        time.sleep(0.5)
                        os.system("cls")
                        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                        print(f"Points : {points}")
                        if points <= 0:
                            print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                            print(f"""
                                Answered   :{answered}
                                Unanswered :{unanswered}
                                Correct    :{correct}
                                Incorrect  :{incorrect}
                                Points      :{points}""")
                            exit()
                        else:
                            continue
        if y == 20:
            levels += 1
            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
            for z in range(31):
                numr = random.randrange(20, 30)
                numl = random.randrange(20, 30)
                Question = input(f"{numl} - {numr} =")
                answer = numl - numr
                Question1 = bool(Question)
                Question2 = Question.isdigit()
                
                if Question1 == False:
                    points -= 2
                    unanswered += 1
                    print("You have not entered the answer to the question\nTherefore you lost 2 points.")
                    time.sleep(0.5)
                    os.system("cls")
                    print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                    print(f"Points : {points}")
                    if points <= 0:
                        print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                        print(f"""
                            Answered   :{answered}
                            Unanswered :{unanswered}
                            Correct    :{correct}
                            Incorrect  :{incorrect}
                            Points     :{points}""")
                        exit()
                    else:
                        continue
                else: 
                    if Question2 == False:
                        points -= 1
                        answered += 1
                        print("You have to enter your answer as a digit and not a character for that you have lost 1 point")
                        time.sleep(0.5)
                        os.system("cls")
                        print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                        print(f"Points : {points}")
                        if points <= 0:
                            print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                            print(f"""
                                Answered   :{answered}
                                Unanswered :{unanswered}
                                Correct    :{correct}
                                Incorrect  :{incorrect}
                                Points     :{points}""")
                            exit()
                        else:
                            continue
                    else:
                        Question = int(Question)
                        if Question == answer:
                            points += 5
                            answered += 1 
                            correct += 1
                            print("Congrats! you haves scored 5 points")
                            time.sleep(0.5)
                            os.system("cls")
                            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                            print(f"Points : {points}")
                        else:
                            points -= 5
                            answered += 1
                            incorrect += 1 
                            print("Opps! Worng answer you have lost 5 points")
                            time.sleep(0.5)
                            os.system("cls")
                            print(f"---------------------------------------------------------LEVEL {levels}---------------------------------------------------------")
                            print(f"Points : {points}")
                            if points <= 0:
                                print("--------------------------------------------------------------------GAME OVER--------------------------------------------------------------------")
                                print(f"""
                                    Answered   :{answered}
                                    Unanswered :{unanswered}
                                    Correct    :{correct}
                                    Incorrect  :{incorrect}
                                    Points     :{points}""")
                                exit()
                            else:
                                continue