#print("Hello AI")
c = 4.2
delta_t = 10
mass = 1
Q = c * mass *delta_t
print(Q)
if Q > 80:
    print("警告:热交换量过大，请检查设备耐受度")
else:
    print("设备运行正常，热交换量在安全范围内")