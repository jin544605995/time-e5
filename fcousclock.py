import time    
import pygame

# 初始化 Pygame    
pygame.init()

# 设置时钟频率    
clock_freq = 1000  # 1000 Hz = 1 frame per second

# 创建一个黑色屏幕    
screen = pygame.display.set_mode((640, 480))

# 创建一个时钟对象    
clock = pygame.time.Clock()

# 定义专注时钟函数    
def focus_clock():    
    # 获取当前时间    
    current_time = time.time()

    # 计算需要显示的时间差    
    time_diff = (current_time - clock.tick(10)) / 10.0

    # 计算需要显示的秒数    
    seconds = int(time_diff * 60)

    # 计算需要显示的分钟数    
    minutes = int((time_diff - seconds) * 60)

    # 绘制当前时间    
    screen.fill((0, 0, 0))    
    pygame.draw.circle(screen, (255, 255, 255), (int(seconds), int(minutes)), 20)    
    pygame.display.update()

# 设置专注时钟函数为每秒调用一次    
focus_clock()

# 循环直到程序退出    
while True:    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:    
            pygame.quit()    
            quit()    
