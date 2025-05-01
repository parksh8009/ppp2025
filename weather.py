import os
import requests

def download_weather_file():
    filename = "weather_146_2020.csv"
    url = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    if not os.path.exists(filename):
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(resp.text)

def get_weather_data(fname, col_idx):
    data = []
    with open(fname, encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.strip().split(",")
            if tokens[col_idx] != "":
                data.append(float(tokens[col_idx]))
    return data

def get_weather_result():
    filename = "weather_146_2020.csv"
    temps = get_weather_data(filename, 2)     # 평균기온
    rains = get_weather_data(filename, 3)     # 강수량

    total_temp = 0
    total_rain = 0
    rain_days = 0

    for t in temps:
        total_temp += t
    for r in rains:
        total_rain += r
        if r >= 5:
            rain_days += 1

    avg_temp = total_temp / len(temps)

    with open("weather_result.txt", "w", encoding="UTF-8") as f:
        f.write("연 평균 기온: " + str(round(avg_temp, 2)) + "도\n")
        f.write("5mm 이상 강우일수: " + str(rain_days) + "일\n")
        f.write("총 강우량: " + str(round(total_rain, 1)) + "mm\n")

def main():
    download_weather_file()
    get_weather_result()

if __name__ == "__main__":
    main()
