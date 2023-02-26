# date related library
from datetime import date

# Endless cycle
while True:
    try:   
        # Get today's date and user's date
        user_date = input("Введите вашу дату рождения (в формате ДД.ММ.ГГГГ): ").split(".")
        today_date = date.today()
        today_day = today_date.day
        today_month = today_date.month
        today_year = today_date.year

        # Determine high year or not
        high_year = "28"
        if int(user_date[2]) % 4 == 0:
            high_year = "29"

        # Checking how many days are in the month of our birth
        daysinmonth = {"1":"31", "2":high_year, "3":"31", "4":"30", "5":"31", "6":"30", "7":"31", "8":"31", "9":"30", "10":"31", "11":"30", "12":"31"}
        days_in_mount = daysinmonth[user_date[1]]

        # Convert user date to numbers
        for el in range(len(user_date)):
            user_date[el] = int(user_date[el])

        # We get data of our age
        years = today_year - user_date[2]
        months = today_month - user_date[1]
        days = today_day - user_date[0]

        # Checking if our age is correct
        if months < 0 or (months == 0 and days < 0):
            years -= 1
            months += 12
        if days < 0:
            months -= 1
            days += int(days_in_mount)

        # Swinging the correct forms of names
        def plural_form(number, one, two_four, five_more):
            if number % 10 == 1 and number % 100 != 11:
                return one
            elif number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
                return two_four
            else:
                return five_more
        years_s = plural_form(years, "год", "года", "лет")
        months_s = plural_form(months, "месяц", "месяца", "месяцев")
        days_s = plural_form(days, "день", "дня", "дней")

        # We check our date for correctness and give the result and break cycle
        if user_date[0] > 31 or user_date[1] > 12 or user_date[2] > today_year:
            print("Вы ввели неправильную дату.\n")
        else:
            print(f"Ваш точный возраст: {years} {years_s}, {months} {months_s}, {days} {days_s}.")
            break

    # Checking user input for correct input
    except KeyError:
        print("Вы ввели неправильную дату.\n")
    except ValueError:
        print("Вы ввели неправильную дату.\n")
    except IndexError:
        print("Вы ввели неправильную дату.\n")
