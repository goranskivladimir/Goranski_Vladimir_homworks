#5)	Вам необходимо написать программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, то результат возвращает False, в противном случае True
healt = int(input('Здоровье персонажа: '))
healt_hero = healt <= 0
if healt_hero:
    print("Надо найти аптечку")
