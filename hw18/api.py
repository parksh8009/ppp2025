import requests
import pandas as pd
from sfarm_hw import submit_to_api

def download_weather(station_id, year, filename):
    url = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def total_rain():
    filename = "weather_146_2012.csv"
    download_weather(146, 2012, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    return round(df["rainfall"].sum(), 1)

def max_of_tmax():
    filename = "weather_146_2024.csv"
    download_weather(146, 2024, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    return round(df["tmax"].max(), 1)

def max_tdiff():
    filename = "weather_146_2020.csv"
    download_weather(146, 2020, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df["tdiff"] = df["tmax"] - df["tmin"]
    return round(df["tdiff"].max(), 1)

def rain_gap():
    f1 = "weather_119_2019.csv"
    f2 = "weather_146_2019.csv"
    download_weather(119, 2019, f1)
    download_weather(146, 2019, f2)
    df1 = pd.read_csv(f1, skipinitialspace=True)
    df2 = pd.read_csv(f2, skipinitialspace=True)
    total1 = df1["rainfall"].sum()
    total2 = df2["rainfall"].sum()
    return round(abs(total1 - total2), 1)

def main():
    name = "박시현"
    affiliation = "스마트팜학과"
    student_id = "202410081"

    answer1 = total_rain()
    answer2 = max_of_tmax()
    answer3 = max_tdiff()
    answer4 = rain_gap()


    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()
