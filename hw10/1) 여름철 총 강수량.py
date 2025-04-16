def sumifs(rainfalls, months, selected=[6,7,8]):
    total=0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total+=rain
    return total

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open (fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_weather_data_int(fname, col_idx):
    weather_datas = []
    with open (fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            # print(tokens[col_idx], type(tokens[col_idx]))
            weather_datas.append(int(tokens[col_idx]))
    return weather_datas

def main():
    filename="./weather(146)_2022-2022.csv"
    rainfalls = get_weather_data(filename,9)
    months =get_weather_data_int(filename, 1)
    print(f'여름철 강수량은 {sumifs(rainfalls, months, selected=[6,7,8]):.1f}입니다 ')


if __name__=="__main__":
    main()