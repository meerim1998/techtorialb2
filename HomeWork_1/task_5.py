min = int(input("Minutes:")) #120

HOUR = 60 
DAY = 24
YEAR = 365

years = min // HOUR // DAY // YEAR # 730(days) // 365(YEAR) = 2years
print("Years:",years)
min_by_year = years * YEAR * DAY * HOUR #6 * 365 * 24 * 60

minutes_after_remove_years = min - min_by_year
days = minutes_after_remove_years // DAY // HOUR
print("Days:",days)






