def timeConversion(s):
    time = s[0:-2].split(':')
    ampm = s[-2:]
    if ampm == 'PM' and time[0] != '12':
        time[0] = str(int(time[0]) + 12)
    elif time[0] == '12':
        time[0] = '00'

    return ':'.join(time)


print(timeConversion('12:01:00PM'))