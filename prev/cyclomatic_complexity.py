import datetime


def print_day_and_month(day: str, month: str):
    print(day)
    print(month)


def date_to_string(year: int, month: int, day: int):
    day_name = ""
    month_name = ""

    if datetime.date(year, month, day).weekday() == 0:
        day_name = "Monday"
    else:
        if datetime.date(year, month, day).weekday() == 1:
            day_name = "Tuesday"
        else:
            if datetime.date(year, month, day).weekday() == 2:
                day_name = "Wednesday"
            else:
                if datetime.date(year, month, day).weekday() == 3:
                    day_name = "Thursday"
                else:
                    if datetime.date(year, month, day).weekday() == 4:
                        day_name = "Friday"
                    else:
                        if datetime.date(year, month, day).weekday() == 5:
                            day_name = "Saturday"
                        else:
                            if datetime.date(year, month, day).weekday() == 6:
                                day_name = "Sunday"

    if month == 1:
        month_name = "January"
    else:
        if month == 2:
            month_name = "February"
        else:
            if month == 3:
                month_name = "March"
            else:
                if month == 4:
                    month_name = "April"
                else:
                    if month == 5:
                        month_name = "May"
                    else:
                        if month == 6:
                            month_name = "June"
                        else:
                            if month == 7:
                                month_name = "July"
                            else:
                                if month == 8:
                                    month_name = "August"
                                else:
                                    if month == 9:
                                        month_name = "September"
                                    else:
                                        if month == 10:
                                            month_name = "October"
                                        else:
                                            if month == 11:
                                                month_name = "November"
                                            else:
                                                if month == 12:
                                                    month_name = "December"

    return f"{day_name} {month_name}, {day} {year}"


if __name__ == "__main__":
    date: str = date_to_string(year=2025, month=7, day=15)
    print(date)
