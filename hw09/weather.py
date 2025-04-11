def read_weather_db(weather):
    tvag_list=[]
    rainfall_list=[]

    with open (weather,encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            tavg = float(tokens[4])
            rainfall = float(tokens[9])
            tvag_list.append(tavg)
            rainfall_list.append(rainfall)

    return tvag_list, rainfall_list

def main():
    tavg, rainfall = read_weather_db("./weather(146)_2022-2022.csv")
    avg_temp=sum(tavg) / len(tavg)
    over_5mm_days= sum (1 for r in rainfall if r>=5.0 )
    total_rain= sum(rainfall)

    print(f'연 평균 기온 : {avg_temp:.1f}℃')
    print(f'5mm이상 강우일수 : {over_5mm_days}일')
    print(f'총 강우량 : {total_rain:.1f}mm')

if __name__ == "__main__":
    main()