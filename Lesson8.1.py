from random import randint
from datetime import datetime
attempts = int(input('Введите количиство попыток: '))
cash = 100

while attempts != 0:
    player = [randint(1, 6), randint(1, 6)]
    comp = [randint(1, 6), randint(1, 6)]
    if cash == 0:
        print('You lost')
        break

    bet = int(input(f"Сделайте ставку: ' \n Доступно:, {cash}"))
    if bet < 1 or bet > cash:
        print('Ставка не должна превыш')
        continue
    attempts -= 1
    if attempts == 0:
        player = [randint(1, 2), randint(1, 3)]
        comp = [randint(1, 6), randint(1, 6)]
    if sum(player) > sum(comp):
        cash += bet
    elif sum(player) < sum(comp):
        cash -= bet
    else:
        pass
    with open('res.txt', 'a') as result:
        result.write(f'player: {player} \n, comp: {comp}, cash: {cash} \n')
    print(cash)
    print('Player: ', player)
    print('Comp: ', comp)

