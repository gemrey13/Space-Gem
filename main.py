import pygame
import time
import random


pygame.font.init()
width, height = 800, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Gem')


bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (width, height))

player_width, player_height = 40, 60
player_velocity = 5

star_width = 10
star_height = 20
star_velocity = 3

font = pygame.font.SysFont('comicsans', 28)


def draw(player, elapsed_time, stars):
    window.blit(bg, (0, 0))

    time_text = font.render(F'Time: {round(elapsed_time)}s', 1, 'white')
    window.blit(time_text, (10, 10))

    pygame.draw.rect(window, 'red', player)

    for star in stars:
        pygame.draw.rect(window, 'white', star)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, height-player_height, player_width, player_height)
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increement = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increement:
            for _ in range(3):
                start_x = random.randint(0,  width - star_width)
                star = pygame.Rect(start_x, -star_height, star_width, star_height) #Star appear on top before the screen
                stars.append(star)

            star_add_increement = max(200, star_add_increement - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_velocity >= 0:
            player.x -= player_velocity
        if keys[pygame.K_RIGHT] and player.x + player_velocity + player_width <= width:
            player.x += player_velocity

        for star in stars[:]:
            star.y += star_velocity
            if star.y > height:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = font.render('You Lost!', 1, 'white')
            window.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)



if __name__ == '__main__':
    main()