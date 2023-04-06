def timeConversion(s):
    mil_time = ''
    if s.endswith('PM') and int(s[:2]) < 12:
        mil_time += str(int(s[:2])+12) + s[2:-2]
        return mil_time
    elif s.endswith('AM') and s.startswith('12'):
        mil_time = '00' + s[2:-2]
        return mil_time
    return s[:-2]

