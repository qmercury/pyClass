"""Turtle 미로 만들기 - 학생용 빈 도화지.

기본 제공: 16×16 격자, 로봇 모양, 한 칸의 이동 거리 STEP.
학생 과제: 벽을 그리고, 벽 좌표를 저장하고, 로봇 이동 코드를 작성합니다.

화면 픽셀 좌표: 왼쪽 위 (0, 0), X는 오른쪽으로, Y는 아래쪽으로 증가.
"""
import turtle
from robot_shape import register_robot_shape

# ===== 선생님이 준비한 기본 환경 =====
GRID_SIZE = 16
CELL_SIZE = 40
STEP = CELL_SIZE

# 화면 좌측 상단과 격자 좌측 상단 모두 픽셀 (0, 0)
START_X = 0
START_Y = 0

screen = turtle.Screen()
screen.setup(800, 800)
screen.title("16 x 16 Maze - Student")
screen.bgcolor("white")

# 일반 Turtle은 가운데가 (0, 0)이고 Y가 위로 증가합니다.
# 수업에서는 이미지 픽셀 좌표처럼 왼쪽 위를 (0, 0)으로 변경합니다.
screen.setworldcoordinates(0, 800, 800, 0)
screen.tracer(0)

# 16×16 격자 (빈 지도)
grid = turtle.Turtle()
grid.hideturtle()
grid.speed(0)
grid.pencolor("lightgray")

for i in range(GRID_SIZE + 1):
    px = START_X + i * CELL_SIZE
    py = START_Y + i * CELL_SIZE

    grid.penup()
    grid.goto(px, START_Y)
    grid.pendown()
    grid.goto(px, START_Y + GRID_SIZE * CELL_SIZE)

    grid.penup()
    grid.goto(START_X, py)
    grid.pendown()
    grid.goto(START_X + GRID_SIZE * CELL_SIZE, py)

grid.penup()

# 미로 안을 돌아다닐 로봇 모양
register_robot_shape(screen)
robot = turtle.Turtle()
robot.shape("maze_robot")
robot.penup()
robot.speed(3)
robot.setheading(0)
robot.goto(20, 20)  # (0, 0)번 셀의 정확한 중앙

screen.update()
screen.tracer(1, 0)


# ======================================================
#               여기부터 학생이 직접 작성
# ======================================================
#
# 미션 1. 검은색 벽을 만드는 코드를 작성하세요.
#         원하는 칸에 벽을 그려 보세요.
#
# 미션 2. 그린 벽의 위치를 (x, y)로 저장하세요.
#         왼쪽 위 칸은 (0, 0), 오른쪽 아래는 (15, 15).
#
# 미션 3. for / if 를 이용해 나만의 미로를 만드세요.
#         시작점 (0, 0)은 막지 마세요.
#
# 미션 4. 로봇을 한 칸(STEP = 40)씩 움직여 보세요.
#         로봇은 각 칸의 중심에 위치해야 합니다.
#
# 미션 5. (심화) 벽이 있으면 로봇이 이동하지 못하게 만드세요.
#


turtle.done()
