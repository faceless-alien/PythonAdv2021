import math
def perimetr(x1, y1, x2, y2, x3, y3):
    first_side=math.sqrt((x1-x2)**2+(y1-y2)**2)
    second_side=math.sqrt((x2-x3)**2+(y2-y3)**2)
    third_side=math.sqrt((x3-x1)**2+(y3-y1)**2)
    return round(first_side+second_side+third_side,6)
print(perimetr(0,0,1,0,0,1))