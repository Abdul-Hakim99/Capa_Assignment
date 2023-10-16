#! /usr/bin/python3

from datetime import datetime


date1_str = input("Please Enter your first date (YYYY-MM-DD): ")
date2_str = input("Please Enter your second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

result = date2 - date1

days_difference = result.days

print(f"Number of days between {date1_str} and {date2_str}: {days_difference} days")

