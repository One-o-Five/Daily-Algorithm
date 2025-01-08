# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# 1901~2000 사이의 100의 배수는 2000 뿐이므로 윤년은 그냥 4의 배수를 구하면 된다.

from datetime import date, timedelta

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

first_sundays = 0
current_date = start_date

while current_date <= end_date:
    
    # 매월 1일이 일요일이면 count
    if current_date.day == 1 and current_date.weekday() == 6:  # 사실 1일인건 확인할 필요가 없지만
        first_sundays += 1
    
    # 다음 달로 이동
    next_month = current_date.month % 12 + 1
    next_year = current_date.year + (current_date.month // 12)
    current_date = date(next_year, next_month, 1)

print (first_sundays)



def is_leap(n):
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        return True
    else:
        return False 
    
def total_days (start_year, year, month, day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    result = 0
    
    # (start_year-1)년 ~ (year-1)년 까지 일수
    for y in range (start_year-1, year):
        result += 365
        if is_leap(y):
            result += 1
            
    # (year)년 1월 ~ (month-1)월 까지 일수        
    for m in range (1, month):
        result += month_days[m-1]
        if (m == 2 and is_leap(year)):
            result += 1
    
    # (month)월 1일 ~ (day)일 까지의 일수
    result += day
    
    return result


def find_first_sundays(start_year, end_year):
    first_sundays = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if (total_days(start_year, year, month, 1)) % 7 == 0:
                first_sundays += 1
    return first_sundays
        
print(find_first_sundays(1901,2000))