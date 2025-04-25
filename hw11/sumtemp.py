def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))
    return weather_datas

def get_weather_date(filename):
    weather_dates = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",") 
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates

def main():
    filename = "./weather(146)_2001-2022.csv"  
    dates = get_weather_date(filename)
    tavg = get_weather_data(filename, 4)

    year_gdd = {}
    base_temp = 5

    for i in range(len(dates)):
        year, month = dates[i][0], dates[i][1]
        if 5 <= month <= 9:
            if tavg[i] >= base_temp:
                if year in year_gdd:
                    year_gdd[year] += tavg[i] - base_temp
                else:
                    year_gdd[year] = tavg[i] - base_temp

    print("연도별 5~9월 GDD:")
    for year in sorted(year_gdd.keys()):
        print(f"{year}   {year_gdd[year]:.1f}")

if __name__ == "__main__":
    main()
