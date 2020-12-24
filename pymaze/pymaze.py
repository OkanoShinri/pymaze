import random
import copy
import os


def pymaze_draw(maze: list,x_min: int = 0, x_max: int = 0, y_min: int =0, y_max:int = 0 ):

    if x_max == 0:
        x_max = len(maze)
    if y_max == 0:
        y_max = len(maze[0])
    if type(maze[0]) is not list:
        print("ERROR:Maze must be 2D array.")
        exit()
    draw_objects = {0: "\u001b[30m ⬛\u001b[0m", 1: "\u001b[37m ⬛\u001b[0m", 2:"\u001b[34m ⬛\u001b[0m", 3:"\u001b[31m ⬛\u001b[0m"}
    for j in range(y_min,y_max):
        for i in range(x_min,x_max):
            print(draw_objects[maze[i][j]], end="")
        print()


def pymaze_makemaze(width: int = 15, height: int = 9) -> list:
    playable = True
    if width % 2 == 0 or height % 2 == 0:
        print("The argument must be an odd number.")
        playable = False
    if width < 7 or height < 7:
        print("The argument must be greater than 6.")
        playable = False
    if not playable:
        exit()

    width += 2
    height += 2

    # 迷路生成(穴掘り法でやる)
    # 壁を1とする
    maze_map = [[1 for _ in range(height)] for _ in range(width)]
    for i in range(width):
        maze_map[i][0] = 0
        maze_map[i][height - 1] = 0
    for i in range(height):
        maze_map[0][i] = 0
        maze_map[width - 1][i] = 0

    # 未探索リスト
    start_points = []
    # 方向リスト(上下左右4方向)
    Directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    current_position = [2, 2]
    maze_map[current_position[0]][current_position[1]] = 0

    # 探索探索ゥ！
    while True:

        moveable_directions = []
        for dr in Directions:
            if maze_map[current_position[0] + 2 * dr[0]][current_position[1] + 2 * dr[1]] == 1:
                moveable_directions.append(dr)

        if len(moveable_directions) == 0:
            if current_position in start_points:
                start_points.remove(current_position)
            if len(start_points) == 0:
                break
            current_position = random.choice(start_points)
        else:
            if len(moveable_directions) == 1:
                if current_position in start_points:
                    start_points.remove(current_position)
            else:
                start_points.append(current_position[:])

            vec = random.choice(moveable_directions)
            maze_map[current_position[0] + 2 * vec[0]][current_position[1] + 2 * vec[1]] = maze_map[current_position[0] + vec[0]][
                current_position[1] + vec[1]] = 0
            current_position[0] += 2 * vec[0]
            current_position[1] += 2 * vec[1]

    # 探索終了
    for i in range(width):
        maze_map[i][0] = 1
        maze_map[i][height - 1] = 1
    for i in range(height):
        maze_map[0][i] = 1
        maze_map[width - 1][i] = 1
    maze_map[2][2] = maze_map[width-3][height-3] = 2
    return maze_map


def pymaze_play(maze: list):
    maze_original = maze
    mypos = [2, 2]

    while True:
        os.system('cls')
        print()
        maze_tmp = copy.deepcopy(maze_original)
        maze_tmp[mypos[0]][mypos[1]] = 3
        pymaze_draw(maze_tmp, mypos[0]-2, mypos[0]+3, mypos[1]-2, mypos[1]+3)


        command = input("command:")
        if command == "W" or command == "w":
            mypos[1] -= 1
        if command == "A" or command == "a":
            mypos[0] -= 1
        if command == "S" or command == "s":
            mypos[1] += 1
        if command == "D" or command == "d":
            mypos[0] += 1
        if command == "E" or command == "e":
            pymaze_draw(maze_tmp)
        if command == "Q" or command == "q":
            break

            
def pymaze(width: int = 15, height: int = 9):
    maze = pymaze_makemaze(width, height)
    # pymaze_draw(maze)
    pymaze_play(maze)

pymaze(19, 15)

