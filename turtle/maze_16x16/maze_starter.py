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
# [명령어 참고] 아래는 설명용 주석입니다.
# 학생들은 주석을 참고해서 직접 코드를 작성하세요.
#
# 1. Turtle 만들기
#    turtle.Turtle()        새로운 그리기용 Turtle 객체 만들기
#    shape("turtle")        Turtle 모양 지정 (robot은 이미 준비됨)
#    hideturtle()           그리기용 Turtle을 화면에서 숨기기
#
# 2. 선 그리기 / 색칠하기
#    penup()                선을 그리지 않고 이동
#    pendown()              선을 그리면서 이동
#    pencolor("black")      선 색상 지정
#    pensize(2)             선 두께 지정
#    fillcolor("black")     사각형 내부 채울 색상 지정
#    begin_fill()           색칠 시작
#    end_fill()             색칠 종료
#
# 3. 위치 이동 (괄호 앞에 사용할 Turtle 이름을 붙입니다)
#    goto(x, y)             (x, y) 픽셀 위치로 이동
#    forward(거리)          바라보는 방향으로 이동 (단위: 픽셀)
#    backward(거리)         반대 방향으로 이동
#    setx(x) / sety(y)      X 또는 Y 좌표만 변경
#
# 4. 방향 바꾸기
#    left(90)               Turtle 기준 왼쪽으로 90도 회전
#    right(90)              Turtle 기준 오른쪽으로 90도 회전
#    setheading(0)          0도(오른쪽 방향)로 맞추기
#    heading()              현재 방향 확인
#    ※ 현재 화면은 Y가 아래로 증가합니다.
#       화면에 보이는 회전 방향을 실행하여 확인해 보세요.
#
# 5. 현재 위치 확인
#    position()             현재 픽셀 좌표 (x, y)
#    xcor()                 현재 X 좌표
#    ycor()                 현재 Y 좌표
#
# 6. 변수, 반복문, 조건문
#    for / range()          정해진 횟수 반복
#    while                  조건이 참인 동안 반복
#    if / elif / else       조건에 따라 동작 선택
#    break / continue       반복 끝내기 / 다음 반복으로 이동
#
# 7. 벽 위치 저장에 사용할 Python 기능
#    set()                  중복 없는 좌표 집합 만들기
#    add()                  집합에 좌표 추가
#    in                     해당 좌표가 저장되어 있는지 검사
#    list / append()        리스트에 좌표 기록하기
#
# [좌표 규칙]
#    화면 왼쪽 위: (0, 0)
#    X는 오른쪽, Y는 아래쪽으로 증가
#    벽 한 칸: 40 x 40픽셀
#    벽의 왼쪽 위 픽셀 좌표 예: (0, 0), (40, 0), (120, 200)
#    로봇은 칸의 중앙으로 이동: (20, 20), (60, 20), (20, 60)
#    STEP = 40 (한 칸 이동 거리)
#
# ======================================================
# 미션 1. 벽 한 칸을 직접 그려 보세요.
# ======================================================
#
#
#
# ======================================================
# 미션 2. 벽의 픽셀 좌표를 기록해 보세요.
# ======================================================
#
#
#
# ======================================================
# 미션 3. 반복문 / 조건문으로 나만의 미로를 만드세요.
# ======================================================
#
#
#
# ======================================================
# 미션 4. 로봇을 STEP만큼 한 칸씩 이동시켜 보세요.
# ======================================================
#
#
#
# ======================================================
# 미션 5. 벽이 있으면 이동하지 않는 코드를 만들어 보세요.
# ======================================================
#
#
#

turtle.done()
