from datetime import datetime

x = input("Date x : ")
y = input("Date y : ")
m = input("Date m : ")

date_format = "%d/%m/%Y"
start = datetime.strptime(x, date_format)
end = datetime.strptime(y, date_format) # Date to be checked
date = datetime.strptime(m, date_format)
delta = date - start
if start <= date <= end:
    status = "true"
else:
    status = "false"
    
print(status,",",delta.days,'Days')