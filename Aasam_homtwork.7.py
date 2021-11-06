import random, time

guesses_made = 0
NumberToGuess = random.randint(1, 100)
userGuess = -1
start = time.time()
while userGuess != NumberToGuess:
    try:
        userGuess = int(input("Угадай число от 1 до 100"))
        if (userGuess < 0 or userGuess > 100):
            print("числа только между 0 и 100")
            continue
    except:
        print("только числа")
        continue
    guesses_made += 1
    if abs(userGuess - NumberToGuess) <= 5:
        print("очень близко ")
    elif abs(userGuess - NumberToGuess) <= 10:
        print("близко ")
    if userGuess > NumberToGuess:

        print("Число должно быть меньше!(<)")
    elif userGuess < NumberToGuess:

        print("Число должно быть больше!(>)")
    else:
        end = time.time()
        print("Вы угадали, это число = " + str(NumberToGuess))
        print("Вы потратили столько попыток", "-", guesses_made)
        print("прошло", round(end - start), "секунд")
        break