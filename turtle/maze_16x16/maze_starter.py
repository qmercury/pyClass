"""16×16 Turtle 미로 만들기 - 학생용 시작 파일.

이 파일은 '격자'와 '로봇 모양'만 준비합니다.
학생이 직접 벽을 그리고, 위치를 저장하고, 로봇 이동을 설계하세요.
"""
import turtle
from robot_shape import register_robot_shape

# ===== 1. 미로 기본 설정 =====
WINDOW_SIZE = 800
GRID_SIZE = 16
CELL_SIZE = 40
STEP = CELL_SIZE

# Turtle 창의 중앙에 640×640 크기의 미로를 배치합니다.
# 왼쪽 위 모서리의 Turtle 좌표: (-320, 320)
START_X = -(GRID_SIZE * CELL_SIZE) / 2
START_Y = (GRID_SIZE * CELL_SIZE) / 2

screen = turtle.Screen()
screen.setup(WINDOW_SIZE, WINDOW_SIZE)
screen.title("16 x 16 Turtle Maze")
screen.bgcolor("white")
screen.tracer(0)

# ===== 2. 16×16 격자 그리기 (기본 제공) =====
grid_pen = turtle.Turtle()
grid_pen.hideturtle()
grid_pen.speed(0)
grid_pen.pencolor("#cbd5dd")
grid_pen.pensize(1)


def draw_grid():
    size = GRID_SIZE * CELL_SIZE
    for index in range(GRID_SIZE + 1):
        px = START_X + index * CELL_SIZE
        py = START_Y - index * CELL_SIZE

        # 세로선
        grid_pen.penup()
        grid_pen.goto(px, START_Y)
        grid_pen.pendown()
        grid_pen.goto(px, START_Y - size)

        # 가로선
        grid_pen.penup()
        grid_pen.goto(START_X, py)
        grid_pen.pendown()
        grid_pen.goto(START_X + size, py)

    grid_pen.penup()


draw_grid()

# ===== 3. 벽 위치를 저장할 집합 =====
# (x, y)는 픽셀 좌표가 아니라 격자 칸 번호입니다.
# 왼쪽 위 (0, 0), 오른쪽 아래 (15, 15)
walls = set()

# 벽을 그리는 전용 Turtle (학생이 사용)
wall_pen = turtle.Turtle()
wall_pen.hideturtle()
wall_pen.speed(0)

# ===== 4. 목표 칸과 로봇 배치 (기본 제공) =====
goal_pen = turtle.Turtle()
goal_pen.hideturtle()
goal_pen.penup()
goal_pen.goto(
    START_X + (GRID_SIZE - 0.5) * CELL_SIZE,
    START_Y - (GRID_SIZE - 0.5) * CELL_SIZE,
)
goal_pen.dot(20, "#efc664")

register_robot_shape(screen)
robot = turtle.Turtle()
robot.shape("maze_robot")
robot.penup()
robot.speed(3)
robot.setheading(0)

# (0, 0)번 칸의 '중앙': Turtle 좌표 (-300, 300)
robot.goto(START_X + CELL_SIZE / 2, START_Y - CELL_SIZE / 2)


# ===== 5. 학생 미션: 벽 한 칸 만들기 =====
def draw_wall(x, y):
    # TODO 1: 격자 좌표 (x, y)를 픽셀 좌표로 바꾸기
    #         힌트: 한 칸은 40픽셀, 왼쪽 위는 (START_X, START_Y)
    # TODO 2: wall_pen으로 해당 칸에 검은 사각형 그리기
    #         힌트: goto, pendown, forward, right, begin_fill, end_fill
    # TODO 3: 벽 위치 (x, y)를 walls에 추가하기
    pass


# ===== 6. 학생 미션: 벽 배치 코드 작성 =====
# 아래 공간에 직접 코드를 추가해 미로를 설계하세요.
# 힌트: draw_wall(열, 행), for, if 등을 사용할 수 있습니다.
#
# 주의: 시작 칸 (0, 0)과 목표 칸 (15, 15)은 비워 두세요.



# ===== 7. 로봇 이동 =====
def forward(step):
    # 현재는 Turtle 로봇이 바라보는 방향으로 이동하기만 합니다.
    # 심화 미션: 이동 전에 다음 칸이 벽인지 확인해 충돌을 방지하세요.
    robot.forward(step)


# 격자/벽을 한꺼번에 표시한 뒤 로봇 이동은 애니메이션으로 보여줍니다.
screen.update()
screen.tracer(1, 0)

# ===== 8. 학생 미션: 로봇 움직이기 =====
# STEP = 40픽셀 = 정확히 한 칸입니다.
# 90도씩 회전하면 로봇이 항상 셀의 중앙을 따라 이동할 수 있습니다.
#
# 예시 명령(주석을 풀어 실험하세요):
# forward(STEP)
# robot.right(90)
# forward(STEP)
#
# 더 나아가기: 벽을 피해 목표 칸까지 이동하는 알고리즘 작성



turtle.done()
