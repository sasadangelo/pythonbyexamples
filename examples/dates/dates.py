from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import pytz

# Print today date
print("---- print today date")
print("Date today =", date.today())
print("Date today (dd/mm/yyyy) =", date.today().strftime("%d/%m/%Y"))

# Get year, month, day of today
print("---- print today year, month, day")
today = date.today()
print("Today year =", today.year)
print("Today month =", today.month)
print("Today day =", today.day)

# Create a date
print("---- print generic date")
mydate = date(2018, 11, 10)
print("mydate =", mydate)
print("mydate year =", mydate.year)
print("mydate month =", mydate.month)
print("mydate day =", mydate.day)

# Delta date
print("---- delta date")
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
print("t1 - t2 =", t1 - t2)

# Print midnight time
print("---- print midnight time")
print("Midnight time =", time())

# Create a time
print("---- print generic time")
mytime = time(10, 11, 00)
print("mytime =", mytime)
print("mytime hour =", mytime.hour)
print("mytime minute =", mytime.minute)
print("mytime secs =", mytime.second)
print("mytime (HH MM SS) =", mytime.strftime("%H %M %S"))

# Print now time
print("---- print now time")
print("Now =", datetime.now())
print("Now (dd/mm/yyyy HH:MM:SS) =", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# Get year, month, day, hour, minute, second, millisecond of now
print("---- print today year, month, day, minute, second of now")
now = datetime.now()
print("Now year =", now.year)
print("Now month =", now.month)
print("Now day =", now.day)
print("Now hour =", now.hour)
print("Now minute =", now.minute)
print("Now secs =", now.second)

# Create a datetime
print("---- print generic datetime")
mydatetime = datetime(2007, 11, 10, 10, 11, 00, 00)
print("mydatetime =", mydatetime)
print("mydatetime year =", mydatetime.year)
print("mydatetime month =", mydatetime.month)
print("mydatetime day =", mydatetime.day)
print("mydatetime hour =", mydatetime.hour)
print("mydatetime minute =", mydatetime.minute)
print("mydatetime secs =", mydatetime.second)

# Delta timw
print("---- delta time")
t1 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t2 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
print("t2 - t1 =", t2 - t1)

# Differences between two dates (or time, or dattime) is a timedelta
print("---- timedelta")
print(timedelta(weeks = 2, days = 5, hours = 1, seconds = 33))

# Manage timezone. You need to install pytz module:
# pip3 install pytz
print("---- timezone")
print("Local now =", datetime.now())
print("New York now =", datetime.now(pytz.timezone('America/New_York')))
print("London now =", datetime.now(pytz.timezone('Europe/London')))
