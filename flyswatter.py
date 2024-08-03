# flyswatter
import math
num = int(input())
for n in range(num):
    f,R,t,r,g = map(float, input().split())
    if g < 2*f:
        print(1)
    else:

        n = math.pi*((R-t)/(g+2*r))**2
        ag = (g**2 - math.pi*f**2) *n
        ar = math.pi*R**2
        p = (ar-ag)/ar
        print(f"ar: {ar}, ag: {ag}, p: {p}")
