
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
    filename ="./weather(146)_2022-2022.csv"
    top3_tmax =sorted(get_weather_data(filename,3))[-3:]
    print(f"가장 높았던 최고기온 3개는 {top3_tmax}℃ 입니다.")

if __name__=="__main__":
    main()
