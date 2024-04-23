''' Write a program that takes a date as input and outputs the date's season
    in the northern hemisphere. The input is a string to represent the month
    and an int to represent the day.
        Spring: March 20 - June 20
        Summer: June 21 - September 21
        Autumn: September 22 - December 20
        Winter: December 21 - March 19
    example:
        April
        11
            output: Spring
        Blue
        65
            output: Invalid
'''
def find_season(month, day):
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November' ,'December')
    months_30_days = ('April', 'June', 'September', 'November')
    # Checking for invalid months/days
    if not(1 <= day <= 31) or not(month in months) or (month in months_30_days and day > 30):
        return 'Invalid'

    # Winter Months
    if (month == 'December' and day >= 21) or (month in ['January', 'February']) or (month == 'March' and day <= 19):
        return 'Winter'
    # Spring Months
    elif (month == 'March' and day >= 20) or (month in ['April', 'May']) or (month == 'June' and day < 21):
        return 'Spring'
    # Summer Months
    elif (month == 'June' and day >= 21) or (month in ['July', 'August'])  or (month == 'September' and day < 22):
        return 'Summer'
    # Autumn Months
    elif (month in ['October', 'November']) or (month == 'September' and day >= 22) or (month == 'December' and day < 21):
        return 'Autumn'
    else:
        return 'Invalid'

input_month = input()
input_day = int(input())
print(find_season(input_month, input_day))

