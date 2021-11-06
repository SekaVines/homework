from random import randint
import datetime

Name = input("Укажите имя?")
attempts = int(input("Сколько попыток?"))
attempts
start_time = datetime.datetime.now()
rnd = 0



while True:
    number1 = randint(1, 9)
    number2 = randint(1, 9)
    Result = number1 * number2
    print(f"Сколько будет {number1} x {number2}")
    try:
        result = int(input())
    except:
        print("только числа")
        continue
    print(Result)
    attempts -= 1
    rnd += 1

    with open('results.txt', 'a') as а:
        if result == Result:
            а.write(f"{number1} x {number2} = {result} ({Result}) правильно\n")
        elif result != Result:
            а.write(f"{number1} x {number2} = {result} ({Result}) неправильно\n")

    if attempts == 0:
        with open('results.txt', 'a') as file:
            file.write(f" попытки: {rnd}, время потрачено: {datetime.datetime.now() - start_time}, имя: {Name}\n")
        break
