import os
import requests
import csv
from sfarm_hw import submit_to_api

def download_weather_file(station_id, year):
    filename = f"weather_{station_id}_{year}.csv"
    url = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    if not os.path.exists(filename):
        resp = requests.get(url)
        resp.encoding = "UTF-8"
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(resp.text)
    return filename

# 1. 2015년 전주시(146)의 총 강수량
def total_rain():
    filename = download_weather_file(146, 2015)
    total = 0.0

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                val = float(row[' rainfall'])  # 공백 주의
            except:
                val = 0.0
            total += val

    return round(total, 1)

# 2. 2022년 전주시(146)의 최대 tavg
def max_of_tavg():
    filename = download_weather_file(146, 2022)
    max_value = -9999  # 아주 작은 값으로 초기화

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                val = float(row[' tavg'])  # 공백 주의
                if val > max_value:
                    max_value = val
            except:
                continue

    return round(max_value, 1)

# 3. 2024년 전주시(146)의 최대 일교차 (tmax - tmin)
def tmax_tmin():
    filename = download_weather_file(146, 2024)
    max_gap = 0.0

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                tmax = float(row[' tmax'])
                tmin = float(row[' tmin'])
                diff = tmax - tmin
                if diff > max_gap:
                    max_gap = diff
            except:
                continue

    return round(max_gap, 1)

# 4. 2024년 수원(119)과 전주(146)의 총 강수량 차이 (절대값)
def gap():
    file1 = download_weather_file(119, 2024)
    file2 = download_weather_file(146, 2024)

    def get_total_rain(filename):
        total = 0.0
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    val = float(row[' rainfall'])
                except:
                    val = 0.0
                total += val
        return total

    r1 = get_total_rain(file1)
    r2 = get_total_rain(file2)
    return round(abs(r1 - r2), 1)

# 제출 함수
def main():
    name = "박시현"
    affiliation = "스마트팜학과"
    student_id = "202410081"

    answer1 = total_rain()
    answer2 = max_of_tavg()
    answer3 = tmax_tmin()
    answer4 = gap()

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4,verbose=True)

if __name__ == "__main__":
    main()
