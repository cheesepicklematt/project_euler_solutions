import pandas as pd
import datetime as dt
sdate = dt.datetime.strptime('1901-01-01','%Y-%m-%d')
edate = dt.datetime.strptime('2000-12-31','%Y-%m-%d')
print("sundays on the first of the month (1901-2000): ",sum([x.weekday()==6 and x.day==1 for x in pd.date_range(sdate,edate-dt.timedelta(days=1),freq='d')]))
