#Problem 6. Leap Years and Days in a Month
  
#(a)Write is_leap(year) that returns True or False
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
#(b)Write days_in_month(month, year) that returns 28, 29, 30 or 31, or None

def days_in_month(month, year):
    if month < 1 or month > 12:
        return None
    elif month == 2:
        return "29" if is_leap(year) else 28
    elif month in (4, 6, 9,  11):
        return "30"
    else:
        return "31"

month = int(input("Enter month as a number: "))
year = int(input("Enter year: "))
print("Month", month, year, ":", days_in_month(month, year))

#c. Print whether 1900, 2000, 2024 and 2026 are leap years.
print()
for y in [1900, 2000, 2024, 2026]:
    print(y, "is a leap year" if is_leap(y) else " is not leap year") 
print("Feb 2024:", days_in_month(2, 2024), "| Feb 2026:", days_in_month(2, 2026),
      "| Apr:", days_in_month(4, 2026), "| month 13:", days_in_month(13, 2026))

   
    
#(d)Count the leap years from 2000 to 2100 (both included) with a loop.
leap_count = 0
for y in range(2000, 2100):
    if is_leap(y):
        leap_count += 1
    
print("Leap year from 2000 t 2100: ", leap_count)
