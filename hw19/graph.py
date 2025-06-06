import requests
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    if not os.path.exists(filename):
        with open(filename, "w", encoding="UTF-8-sig") as f:
            resp = requests.get(URL)
            resp.encoding = "UTF-8"
            f.write(resp.text)

def main():
    station_id = 146 
    all_data = []

    # 1980~2024년 기상데이터 수집
    for year in range(1980, 2025):
        filename = f"weather_{station_id}_{year}.csv"
        download_weather(station_id, year, filename)
        df = pd.read_csv(filename, skipinitialspace=True)
        df["year"] = year
        all_data.append(df)

    df_all = pd.concat(all_data)

    # -----------------------------
    # 1. 여름 vs 겨울 기온 히스토그램
    # -----------------------------
    summer = df_all[df_all["month"].isin([6, 7, 8])]
    winter = df_all[df_all["month"].isin([12, 1, 2])]

    plt.hist(summer["tavg"].dropna(), bins=30, alpha=0.7, label="여름")
    plt.hist(winter["tavg"].dropna(), bins=30, alpha=0.7, label="겨울")
    plt.xlabel("평균기온(℃)")
    plt.ylabel("빈도")
    plt.title("여름 vs 겨울 평균기온 분포 (1980-2024)")
    plt.legend()
    plt.savefig("season_temp_hist.png")
    plt.show()

    # -----------------------------
    # 2. 생일 기온 변화 그래프
    # -----------------------------
    birthday = df_all[(df_all["month"] == 7) & (df_all["day"] == 22)].copy()
    birth_year = 2005  # 본인의 출생년도
    birthday["age"] = birthday["year"] - birth_year

    fig, ax = plt.subplots()
    ax.plot(birthday["year"], birthday["tmax"], color="red", label="최고기온")
    ax.plot(birthday["year"], birthday["tmin"], color="blue", label="최저기온")
    ax.axvline(birth_year, color="gray", linestyle="--", label="출생년도")
    ax.set_ylabel("기온(℃)")
    ax.set_xlabel("년도")
    ax.set_title("내 생일(7월 22일) 기온 변화")
    ax.legend()
    plt.savefig("birthday_temp_trend.png")
    plt.show()


    # -----------------------------
    # 3. 가장 더웠던/추웠던 생일 출력
    # -----------------------------
    birthday_clean = birthday.dropna(subset=["tmax", "tmin"])
    if len(birthday_clean) == 0:
        print("생일 데이터가 없습니다.")
    else:
        hottest = birthday_clean.sort_values("tmax", ascending=False).iloc[0]
        coldest = birthday_clean.sort_values("tmin").iloc[0]

        print(f"가장 더웠던 생일: {int(hottest['year'])}년 , 최고기온 {hottest['tmax']}℃")
        print(f"가장 추웠던 생일: {int(coldest['year'])}년 , 최저기온 {coldest['tmin']}℃")

if __name__ == "__main__":
    main()