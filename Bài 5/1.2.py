import datetime as dt
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2006-12-26T13:02:55',format)
print('Day:'+str(t1.day))
#tương tự in month minute second

t2 = dt.datetime.now()
khoang_cach = t2-t1
print('số ngày cách xa: '+ str(khoang_cach.days))



