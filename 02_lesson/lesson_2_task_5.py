def month_to_season(i):
    if 1 <= i <= 2 or i == 12:
        print('Зима')
    elif 3 <= i <= 5:
        print('Весна')
    elif 6 <= i <= 8:
        print('Лето')
    elif 9 <= i <= 11:
        print('Осень')
