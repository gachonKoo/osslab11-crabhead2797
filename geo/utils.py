import math

def pythagoras(a, b):
    # 피타고라스 정리
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    # 정밀도 문제 해결을 위해 고정 PI 값 사용
    PI = 3.141592653589793
    area = PI * r**2
    return area
