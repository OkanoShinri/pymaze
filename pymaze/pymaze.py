import random


def pyMaze_draw(maze: list):
    if type(maze[0]) is not list:
        print("ERROR:Maze must be 2D array.")
        exit()
    DrawObjects = {0: " ⬜", 1: " ⬛", 2:" 🟦"}
    for j in range(len(maze[0])):
        for i in range(len(maze)):
            print(DrawObjects[maze[i][j]], end="")
        print()


def pyMaze_makemaze(width: int = 15, height: int = 9) -> list:
    playable = True
    if width % 2 == 0 or height % 2 == 0:
        print("The argument must be an odd number.")
        playable = False
    if width < 7 or height < 7:
        print("The argument must be greater than 7.")
        playable = False
    if not playable:
        exit()

    width += 2
    height += 2

    # 迷路生成(穴掘り法でやる)
    # 壁を1とする
    MazeMap = [[1 for _ in range(height)] for _ in range(width)]
    for i in range(width):
        MazeMap[i][0] = 0
        MazeMap[i][height - 1] = 0
    for i in range(height):
        MazeMap[0][i] = 0
        MazeMap[width - 1][i] = 0

    # 未探索リスト
    StartPoints = []
    # 方向リスト(上下左右4方向)
    Directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    CurrentPos = [2, 2]
    MazeMap[CurrentPos[0]][CurrentPos[1]] = 0

    # 探索探索ゥ！
    while True:

        moveableDirections = []
        for dr in Directions:
            if MazeMap[CurrentPos[0] + 2 * dr[0]][CurrentPos[1] + 2 * dr[1]] == 1:
                moveableDirections.append(dr)

        if len(moveableDirections) == 0:
            if CurrentPos in StartPoints:
                StartPoints.remove(CurrentPos)
            if len(StartPoints) == 0:
                break
            CurrentPos = random.choice(StartPoints)
        else:
            if len(moveableDirections) == 1:
                if CurrentPos in StartPoints:
                    StartPoints.remove(CurrentPos)
            else:
                StartPoints.append(CurrentPos[:])

            vec = random.choice(moveableDirections)
            MazeMap[CurrentPos[0] + 2 * vec[0]][CurrentPos[1] + 2 * vec[1]] = MazeMap[CurrentPos[0] + vec[0]][
                CurrentPos[1] + vec[1]] = 0
            CurrentPos[0] += 2 * vec[0]
            CurrentPos[1] += 2 * vec[1]

    # 探索終了
    for i in range(width):
        MazeMap[i][0] = 1
        MazeMap[i][height - 1] = 1
    for i in range(height):
        MazeMap[0][i] = 1
        MazeMap[width - 1][i] = 1
    MazeMap[2][2] = MazeMap[width-3][height-3] = 2
    return MazeMap


def pyMaze_play(maze: list):
    origimalMaze = maze
    mypos = [2, 2]

    while True:
        tmpMaze = origimalMaze
        command = input()
        if command == "W" or command == "w":
            mypos[1] -= 1
        if command == "A" or command == "a":
            mypos[0] -= 1
        if command == "S" or command == "s":
            mypos[1] += 1
        if command == "D" or command == "d":
            mypos[0] += 1
        if command == "E" or command == "e":
            pass
        if command == "Q" or command == "q":
            break



def pyMaze(width: int = 15, height: int = 9):
    maze = pyMaze_makemaze(width, height)
    pyMaze_play(maze)

pyMaze(19, 15)
