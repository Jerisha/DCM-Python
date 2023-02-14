from datetime import datetime, timedelta

now=datetime.now()
currentDate=now.replace(hour=0, minute=0, second=0, microsecond=0)
print('Input date:', currentDate.strftime("%Y%m%d"))

# move to first next month
next_month = currentDate.replace(day=28) + timedelta(days=4)

# come back to the first next month's last day
res = next_month - timedelta(days=next_month.day)
print('Last day of the next month:', res.date().strftime("%Y%m%d"))