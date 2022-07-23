import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm
b = mc
c = bm
a = bc
angle_b_radian = math.acos(a / (2*b))
angle_b_degree = int(round((180 * angle_b_radian) / math.pi))
output_str = str(angle_b_degree)+'°'
print(output_str)
