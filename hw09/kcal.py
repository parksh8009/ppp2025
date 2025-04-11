def read_kcal_db(fruit):
    kcal_dic={}
    with open (fruit, encoding="utf-8-sig") as f:
        lines=f.readlines()
        
        for line in lines[1:]:
            line=line.strip()
            tokens = line.split(",")
            kcal_dic[tokens[0]] = int(tokens[1])
    
    return kcal_dic

def main():
    fruit_cal=read_kcal_db("./calorie_db.csv")
    fruit_eat={"쑥":150, "바나나":200}
    total=0
    for fruit in fruit_eat:
        total+=(fruit_cal[fruit]*fruit_eat[fruit])
    print(f"총 칼로리는 {total}kcal 입니다.")

if __name__ == "__main__":
    main()