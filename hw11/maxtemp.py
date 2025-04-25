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
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)

    year_max_gap = {}

    for i in range(len(dates)):
        year = dates[i][0]
        gap = tmax[i] - tmin[i]
        if year in year_max_gap:
            if gap > year_max_gap[year][1]:
                year_max_gap[year] = (dates[i], gap)
        else:
            year_max_gap[year] = (dates[i], gap)

    print("연도별 최대 일교차:")
    for year in sorted(year_max_gap.keys()):
        date, gap = year_max_gap[year]
        print(f"{date[0]}/{date[1]:02d}/{date[2]:02d}  {gap:.1f}")

if __name__ == "__main__":
    main()
