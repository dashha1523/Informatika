salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Подушка безопасности
monthss = months # остаток месяцев
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while monthss != 0:
    money_capital = money_capital + salary - spend
    spend = spend * (1 + increase) #расходы
    monthss -= 1
money_capitall = int(money_capital) #округление
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", -money_capitall)
