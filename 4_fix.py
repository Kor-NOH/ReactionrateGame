import os
import pygame

# 기본 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1100 # 창 가로 크기
screen_height = 600 # 창 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("반응속도 게임") #게임 이름

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트, 속도 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # 이미지 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character_R.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - (character_height + stage_height)

# 캐릭터 이동 방향
character_to_x = 0

# 이동 속도
character_speed = 5

# 적 캐릭터
enemy = pygame.image.load(os.path.join(image_path, "enemy.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width
enemy_y_pos = 0 + enemy_height

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10



# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)  # 게임 화면의 초당 프레임 수를 설정


    print("fps : ", str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였으면
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 0.5 # x 좌표를 뺌
            if event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽
                to_x += 0.5  # x 좌표를 더함
            if event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= 0.5
            if event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += 0.5

        if event.type == pygame.KEYUP: # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 캐릭터가 가로 창밖을 못벗어남
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > 1100 - character_width:
        character_x_pos = 1100 - character_width

    # 캐릭터가 세로 창밖을 못벗어남
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > 600 - character_height:
        character_y_pos = 600 - character_height



    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, (screen_height - stage_height)))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()


