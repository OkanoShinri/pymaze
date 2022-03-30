import random
import copy
import os
import time
import argparse
import readchar


def draw(
    maze: list, x_min: int = 0, x_max: int = 0, y_min: int = 0, y_max: int = 0
) -> None:
    if type(maze[0]) is not list:
        print("ERROR:Maze must be 2D array.")
        exit()
    if x_max == 0:
        x_max = len(maze)
    if y_max == 0:
        y_max = len(maze[0])

    draw_objects = {
        0: "\u001b[40m  \u001b[0m",
        1: "\u001b[47m  \u001b[0m",
        2: "\u001b[44m  \u001b[0m",
        3: "\u001b[31m〇\u001b[0m",
    }
    for j in range(y_min, y_max):
        for i in range(x_min, x_max):
            print(draw_objects[maze[i][j]], end="")
        print()


def makemaze(width: int = 15, height: int = 9, draw_process: bool = False) -> list:
    playable = True
    if width % 2 == 0 or height % 2 == 0:
        print("The argument must be an odd number.")
        playable = False
    if width < 7 or height < 7:
        print("The argument must be greater than 6.")
        playable = False
    if not playable:
        exit()

    is_draw_process = draw_process

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
            if (
                maze_map[current_position[0] + 2 * dr[0]][
                    current_position[1] + 2 * dr[1]
                ]
                == 1
            ):
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
            maze_map[current_position[0] + 2 * vec[0]][
                current_position[1] + 2 * vec[1]
            ] = 0
            maze_map[current_position[0] + vec[0]][current_position[1] + vec[1]] = 0
            current_position[0] += 2 * vec[0]
            current_position[1] += 2 * vec[1]
            if is_draw_process:
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                draw(maze_map)
                time.sleep(0.1)

    # 探索終了
    for i in range(width):
        maze_map[i][0] = 1
        maze_map[i][height - 1] = 1
    for i in range(height):
        maze_map[0][i] = 1
        maze_map[width - 1][i] = 1
    maze_map[2][2] = maze_map[width - 3][height - 3] = 2
    return maze_map


def play(maze: list) -> None:
    maze_original = maze
    maze_currentmap = [[1 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    mypos = [2, 2]

    while True:
        if mypos == [len(maze_original) - 3, len(maze_original[0]) - 3]:
            draw(maze_original)
            print("Congratulations!")
            input("Press Enter key")
            break

        maze_minimap = copy.deepcopy(maze_original)
        maze_minimap[mypos[0]][mypos[1]] = 3
        maze_currentmap[mypos[0]][mypos[1]] = 0

        # 周囲4マスで「道があるが未到達」のマスを青色に
        for i in [-1, 1]:
            if (
                maze_minimap[mypos[0] + i][mypos[1]] == 0
                and maze_currentmap[mypos[0] + i][mypos[1]] == 1
            ):
                maze_currentmap[mypos[0] + i][mypos[1]] = 2
            if (
                maze_minimap[mypos[0]][mypos[1] + i] == 0
                and maze_currentmap[mypos[0]][mypos[1] + i] == 1
            ):
                maze_currentmap[mypos[0]][mypos[1] + i] = 2

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("===========")
        draw(maze_minimap, mypos[0] - 2, mypos[0] + 3, mypos[1] - 2, mypos[1] + 3)
        print("===========")
        print("q:quit  w:up    e:map")
        print("a:left  s:down  d:right")
        print("command: ", end="", flush=True)
        command = readchar.readchar()

        if command == "W" or command == "w":
            if maze_minimap[mypos[0]][mypos[1] - 1] != 1:
                mypos[1] -= 1
        elif command == "A" or command == "a":
            if maze_minimap[mypos[0] - 1][mypos[1]] != 1:
                mypos[0] -= 1
        elif command == "S" or command == "s":
            if maze_minimap[mypos[0]][mypos[1] + 1] != 1:
                mypos[1] += 1
        elif command == "D" or command == "d":
            if maze_minimap[mypos[0] + 1][mypos[1]] != 1:
                mypos[0] += 1
        elif command == "E" or command == "e":
            print()
            maze_currentmap[mypos[0]][mypos[1]] = 3
            draw(maze_currentmap)
            input("Press Enter key ...")
            maze_currentmap[mypos[0]][mypos[1]] = 0
        elif command == "R" or command == "r":
            r = input("スタート地点に戻りますか？(y/n):")
            if r == "Y" or r == "y":
                mypos = [2, 2]
        elif command == "Q" or command == "q":
            q = input("ゲームを終了しますか？(y/n):")
            if q == "Y" or q == "y":
                break
        elif command == "C":  # cheat
            draw(maze_minimap)
            input("Press Enter key ...")


def run(width: int = 31, height: int = 31, process: bool = False) -> None:
    maze = makemaze(width, height, process)
    play(maze)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-w", "--width", type=int, default=31, help="横幅")
    parser.add_argument("-hi", "--height", type=int, default=31, help="縦幅")
    parser.add_argument("--process", action="store_true", help="生成過程を表示するか")
    args = parser.parse_args()

    run(args.width, args.height, args.process)
