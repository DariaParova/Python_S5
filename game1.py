from random import randint

def input_dat(name):
    x = int(
        input("Введите количество конфет от 1 до 28: "))
    return x


def p_print(name, k, counter, value):
    print(f"{name} взял {k}, теперь у него {counter}. На столе осталось {value} конфет.")


player1 = input("Введите ваше имя: ")
player2 = "Bot"
value = int(input("Введите общее количество конфет на столе: "))
step = randint(0, 2)
if step:
    print(f"Первый ход {player1}")
else:
    print(f"Первый ход {player2}")

count1 = 0
count2 = 0

while value > 28:
    if step:
        k = input_dat(player1)
        count1 += k
        value -= k
        step = False
        p_print(player1, k, count1, value)
    else:
        k = randint(1, 29)
        count2 += k
        value -= k
        step = True
        p_print(player2, k, count2, value)

if step:
    print(f"Поздравляю, {player1}, вы выйграли!")
else:
    print(f"Победу одержал {player2}")