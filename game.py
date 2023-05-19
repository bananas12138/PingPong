import pygame
import random
import time


pygame.init()  # 初始化pygame

# 定义ball_restart函数
def ball_restart():
    global ball_speed_x, ball_speed_y, ball
    ball.center = (395, 295)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((800, 600))

# 标题和图标
pygame.display.set_caption("Ping Pong")

# 矩形框
paddle_a = pygame.Rect(5, 5, 10, 100)
border_a = pygame.Rect(0, 0, 20, 110)

paddle_b = pygame.Rect(785, 5, 10, 100)
border_b = pygame.Rect(770, 0, 20, 110)

# 圆形球
ball = pygame.Rect(395, 295, 10, 10)

# 速度变量
ball_speed_x = 1 * random.choice((1, -1))
ball_speed_y = 1 * random.choice((1, -1))

# 移动球拍
paddle_a.y -= 1
if paddle_a.top < border_a.top:
    paddle_a.top = border_a.top

paddle_a.y += 1
if paddle_a.bottom > border_a.bottom:
    paddle_a.bottom = border_a.bottom

paddle_move_count = 0

if paddle_move_count < 10:  # 10帧内只移动一次
    paddle_a.y -= 2
    paddle_move_count += 1
else:
    paddle_move_count = 0

# 玩家A分数
score_a = 0
# 玩家B分数
score_b = 0

# 游戏循环
run = True
while run:

    # 屏幕背景颜色
    screen.fill((0, 0, 0))

    # 绘制矩形框(球拍)
    pygame.draw.rect(screen, (255, 255, 255), paddle_a)
    pygame.draw.rect(screen, (255, 255, 255), paddle_b)

    # 绘制圆形球
    pygame.draw.circle(screen, (255, 255, 255), (ball.x, ball.y), 10)

    # 移动球拍
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_w]:
        paddle_a.y -= 5
    if key_pressed[pygame.K_s]:
        paddle_a.y += 5
    if key_pressed[pygame.K_UP]:
        paddle_b.y -= 5
    if key_pressed[pygame.K_DOWN]:
        paddle_b.y += 5

        # 移动球
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 碰撞检测
    # 球碰撞上下墙
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1

    # 球碰撞球拍
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # 球没打中,相应方加1分
    if ball.left <= 0:
        score_b += 1
        ball_restart()
    if ball.right >= 800:
        score_a += 1
        ball_restart()

    # 显示分数
    font = pygame.font.Font(None, 74)
    text = font.render(str(score_a), 1, (255, 255, 255))
    screen.blit(text, (250, 10))
    text = font.render(str(score_b), 1, (255, 255, 255))
    screen.blit(text, (520, 10))

    # 更新屏幕
    pygame.display.flip()

    # 检测关闭窗口事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # 结束pygame
pygame.quit()