import re

def str_to_day(DATE):
    month = re.findall('^2020-([0-9]+)-', DATE)
    month = int(month[0])
    day = re.findall('^2020-[0-9]+-([0-9]+)', DATE)
    day = int(day[0])
    if month==1:
        DAY = day - 25 + 1
    elif month==2:
        DAY = 7 + day 
    elif month==3:
        DAY = 7 + 29 + day
    else:
        DAY = 7 + 29 + 31 + day 
    return DAY


def day_to_str(DAY):
    if DAY<=7:
        month = 1
        day = 25 + DAY - 1 
    elif DAY<=36:
        month = 2
        day = DAY - 7
    elif DAY<=67:
        month = 3
        day = DAY - 36
    else:
        month = 4
        day = DAY - 67
    month = str(month)
    day = str(day)
    if int(day)<10:
        DATE = "2020-0"+month+"-0"+day
    else:
        DATE = "2020-0"+month+"-"+day
    return(DATE)
