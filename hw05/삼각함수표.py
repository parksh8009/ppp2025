import math

print("각도(°)  | 라디안 |  sin  |   cos   |  tan")
print("-" * 50)

for i in range(0, 91, 1): 
    radian = math.radians(i) 
    sin = math.sin(radian)
    cos = math.cos(radian) 
    tan = math.tan(radian)

    print(f"{i:4f} | {radian:.4f} | {sin:.4f} | {cos:.4f} | {tan:.4f}")
