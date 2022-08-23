#what day of the week you were born.

def information(year, month, day):
    if month == 1 or month == 2 :
        year = year - 1
        month = month + 12
    cul = (year + (year // 4) - (year // 100) + (year // 400) + ((13*month+8) // 5) + day) % 7  #from Zeller's fomular
    return cul

weekday = information(int(input("year >")), int(input("month >")), int(input("day >")))


order = {0:"Sun", 1:"Mon", 2:"Tue", 3:"Wed", 4:"Fri", 5:"Stu"}

if weekday in order:
    ans = order[weekday]
    print('\033[32m' + ans + '\033[0m')
else:
    None