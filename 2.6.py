import math
R=6350
print("Введите высоту над Землей")
d=float(input())
H=math.sqrt((R+d)*(R+d)-R*R)
print(H)
