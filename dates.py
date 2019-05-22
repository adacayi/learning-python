from datetime import datetime, timedelta
from pytz import timezone

now = datetime.now()
print(now)
print()
print(now.year)
print(now.strftime("%A"))
print(now.strftime("%B"))
# print(now.strftime("%C"))
# print(now.strftime("%D"))

print()
firstOfMay = datetime(2019, 5, 1)
print(firstOfMay)
firstOfMay = firstOfMay + timedelta(hours=2, minutes=34, seconds=59)
print(firstOfMay)
firstOfMay = firstOfMay.replace(tzinfo=timezone("UTC"))
print(firstOfMay.strftime("%a, %d %b %Y %H:%M:%S %Z"))

"""
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%
"""
