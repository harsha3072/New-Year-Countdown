month_day = [['Jan',31], ['Feb',28], ['Mar',31], ['Apr',30], ['May',31],
['Jun',30],['Jul',31], ['Aug',31],['Sep',30], ['Oct',31],['Nov',30],['Dec',31]]
# enter string of user
mon, day, year, time, am_pm = input().split()
# leap year check
y = int(year)
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    month_day[1][1] =28
else:
    month_day[1][1] =29
# get full day 
day, after = int(day), 0
for item in month_day:
    day += item[1] * after
    if item[0] == mon:
        day = item[1]- day
        after = 1
# detect hours and minutes 
hour, min = time.split(':')
if int(min) != 0:
    min = 60 - int(min)
else:
    min = 0
if am_pm == 'PM':
    hour = 12 -int(hour)
if am_pm == 'AM':
    hour = 24 -int(hour)
if min !=0:
    hour -= 1
# output result
print(f'{24*day + hour} hours {min} minutes')
