import datetime

def GetStrDate():
    date = datetime.date.today()
    datestr = date.strftime("%Y%m%d")

    return datestr 

def StrDateToInt(date_str):

    dateint = 0
    for i in range(len(date_str)-8, len(date_str)):
        dateint = dateint*10 + int(date_str[i])
    
    return dateint

def UpdateToken(id):
    date_str = GetStrDate()
    date_int = StrDateToInt(date_str)

    letter = date_int % 26
    token_A = chr(letter+65)
    token_B = date_int * id
    token_B = StrDateToInt(str(token_B))

    tokenstr = token_A + "-" + str(token_B)
    return tokenstr
