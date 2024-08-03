# problem
import math
num = int(input())

for n in range(num):
    left = int(input())
    right = 0
    left_weights = []
    right_weights = []
    while left != right:

        if left > right:
            weight_right = 3**round(math.log((left-right),3))
            right = right + weight_right
            right_weights.append(weight_right)
        elif right > left:
            weight_left = 3**round(math.log((right-left),3))
            left = left + weight_left
            left_weights.append(weight_left)


    left_pan = "left pan:"
    for wl in left_weights:
        left_pan  = left_pan + " " + str(wl)
    print(left_pan)

    right_pan = "right pan:"
    for wr in right_weights:
        right_pan  = right_pan + " " + str(wr)
    print(right_pan)

    if n < num-1:
        print("\n")

        


