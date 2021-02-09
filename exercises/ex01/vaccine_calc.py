"""A vaccination calculator."""

__author__ = "730238353"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: str = input("What is the current population?")
dose_admin: str = input("How many doses have already been given to the population?")
dose_rate: str = input("How many doses are given per day?")
target: str = input("What is the target vaccination proportion?")

pop_int = int(population) 
admin_int = int(dose_admin)
pop_remain: int = (pop_int - admin_int) 



today: datetime = datetime.today()
print(today)
today.strftime("%B %d, %Y")
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day 
print(tomorrow.strftime("%B %d, %Y"))
fortnight: timedelta = timedelta(7 + 7)
future: datetime = today + fortnight 