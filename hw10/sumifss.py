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

def sumifs(rainfalls, months, selected=[6,7,8]):
    total=0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total+=rain
    return total

def main():
    filename="./weather(146)_2022-2022.csv"
    filename_20yr = './weather(146)_2001-2022.csv'
    years=get_weather_data_int(filename_20yr, 0)
    rainfalls=get_weather_data(filename_20yr, 9)
    print(f"2021년 총 강수량은 {sumifs(rainfalls, years, selected=[2021]):.1f}mm")
    print(f"2022년 총 강수량은 {sumifs(rainfalls, years, selected=[2022]):.1f}mm")


if __name__=="__main__":
    main()
