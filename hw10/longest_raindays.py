def longest_raindays(rainfalls):
    events=[]
    c_days=0
    for rain in rainfalls:
        if rain > 0 :
            c_days += 1
        else:
            if c_days > 0 :
                events.append(c_days)
            c_days = 0
    if c_days > 0 :
        events.append(c_days)
    return events

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open (fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def main ():
    filename='./weather(146)_2022-2022.csv'
    rainfalls = get_weather_data(filename,9)
    print(f"최장 연속 강우 일수 = {max(longest_raindays(rainfalls))}일")

if __name__ == '__main__':
    main()
