# EscapeWallMaria
t,row,col = map(int,input().split())
time = 0
wall = []
visited = [wall]

def valid_move(vis, dir, r, c):
    loc = visited[row][col]
    if loc == "1":
        return False
    elif loc == "0":
        return True
    elif loc == "U" and dir == "down":
        return True
    elif loc == "D" and dir == "up":
        return True
    elif loc == "L" and dir == "right":
        return True
    elif loc == "R" and dir == "left":
        return True
    else:
        print("why am I here?")




for r in range(row):
    wall.append([*input()])

# movement
if (r == 0 or r == row-1 or c == 0 or c == col-1):
    pass
print(wall)

# while time < t:
#     time = time + 1

