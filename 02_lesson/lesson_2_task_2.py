def is_year_leap(y):
    if int(y) % 4 == 0:
        return True
    else:
        return False


yr = input("Введите год:")
res = str(is_year_leap(yr))
print("год " + yr + ": " + res)
