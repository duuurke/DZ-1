def month_to_season(a):
    if a == 1 or a == 2 or a == 12:
        return ("зима")
    if a == 3 or a == 4 or a == 5:
        return ("весна")
    if a == 6 or a == 7 or a == 8:
        return ("лето")
    if a == 9 or a == 10 or a == 11:
        return ("осень")
    else:
        return ("укажите правильный номер месяца")


print(month_to_season(int(input('введите номер месяца '))))
