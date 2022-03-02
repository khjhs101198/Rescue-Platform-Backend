import datetime

def datetimeTOint():
    date = datetime.date.today()
    datestr = date.strftime("99%Y%m%d")
    dateint = 0
    for i in range(len(datestr)-8, len(datestr)):
        dateint = dateint*10 + int(datestr[i])
    
    return dateint
datetimeTOint()