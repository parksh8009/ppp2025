import random

def problem():
    dan = random.randint(2,9)
    mul = random.randint(1,9) 

    try:
        ans = int(input(f"{dan} x {mul}=? "))
    except ValueError:
        return False

    


    # ans=int(input(f"{dan}*{mul}=?"))

    if ans == dan * mul:
        #print("정답")
        return True
    #print("오답")
    return False



def main():
    score = 0
    total_problem = 5
    for n in range(total_problem):
        is_correct = problem()
        if is_correct:
            score +=1
    print(f"총점은 {score}, {score / total_problem *100}점")


if __name__ == "__main__":
    main()