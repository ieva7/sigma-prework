import datetime
import math

currentYear = int(datetime.date.today().year)

theirTime = input("Please enter the date for which you'd like to calculate the age in format dd-mm-yyyy.\n")
theirYear = int(theirTime.split('-')[2])
difference = abs(currentYear-theirYear)

print(f"The difference between your specificied date and the date today is {difference} year(s)")


