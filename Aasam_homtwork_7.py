import random, time
guesses_made = 0
NumberToGuess = random.randint(1, 100)
userGuess=-1
start = time.time()
while userGuess != NumberToGuess:
    try:
        userGuess = int(input("Угадай число от 1 до 100"))

        if userGuess > NumberToGuess:
            print("Число должно быть меньше!")
            continue
    except:
        print("только числа")
        continue
        guesses_made += 1
  # elif userGuess < NumberToGuess:
        print("Число должно быть больше!")
    else:
        end = time.time()
        print("Вы угадали, это число = " + str(NumberToGuess))
        print("Вы потратили столько попыток", "-", guesses_made)
        print("прошло", round(end-start), "секунд")
        break


