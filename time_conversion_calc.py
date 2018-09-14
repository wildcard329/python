
day = 0
hour = 0
minute = 0
sec = 0

def convert():
    print(str(day) + ' days ' + str(hour) + ' hours ' + str(minute) + ' minutes ' + str(sec) + ' seconds')

time = int(input('Enter time in seconds ')) 

if time < 60:
    sec = time
    convert()
elif time >= 60 and time < 3600:
    minute = time // 60
    sec = time % 60
    convert()
elif time >= 3600 and time < 86400:
    hour = time // 3600
    rr = time % 3600
    minute = rr // 60
    rr = time % 60
    sec = rr
    convert()
elif time >= 86400:
    day = time // 86400
    rr = time % 86400
    hour = rr // 3600
    rr = rr % 3600
    minute = rr // 60
    sec = rr % 60
    convert()
else:
    pass
