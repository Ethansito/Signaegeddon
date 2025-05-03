import cv2
import cv2 as cv
import numpy as np
import pygame
from numpy import *
from pygame import SRCALPHA
from wonderwords import RandomWord

import AlphaTrackModule as atm
import FingerCounterModule as fcm
import GameObjects
import HandTrackModule as htm

if __name__ == "__main__":
    text, character = "", ""
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    detector = htm.handDetector()

    def on_lock_in(lm_list):
        global text
        text = text.replace('_', ' ', 1)
        text += atm.readAlpha(lm_list)

    def clear_text():
        global text
        text = ""

    def asteroid_spawner(start_time, needed_time):
        the_time = int(pygame.time.get_ticks())
        if the_time - start_time >= needed_time:
            word = generator.word()
            speed = fmax(1 - len(word) * 0.1, 0.1) # Asteroids with longer words move slower
            GameObjects.Asteroid(word, speed).spawn()
            return the_time
        return start_time

    # Random Words
    letters = ["a", "y"]
    generator = RandomWord(letter=letters)

    # Pygame Setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Signaegeddon")
    clock = pygame.time.Clock()
    dt = 0
    base_time = 0
    time_requirement = 10000

    player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
    player_surf = pygame.Surface((80, 80), SRCALPHA)
    pygame.draw.circle(player_surf, "green", (40, 40), 40)
    player_rect = player_surf.get_rect(center=player_pos)
    player_rect.inflate_ip(-30, -30)

    # Score/Health
    health = 12
    scoreboard = GameObjects.Scoreboard(health)
    scoreboard_text = pygame.font.Font(None, 100).render("Score\n    " + str(scoreboard.score), True, "white")

    running = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if running:
            success, img = cap.read()
            img = detector.findHands(img)

            lmList = fcm.finger_count(img, detector, on_lock_in, clear_text)

            character = "" if len(lmList) == 0 else atm.readAlpha(lmList)

            if success:
                cv.putText(img, text, (28, 468), cv.FONT_HERSHEY_PLAIN,
                        4, (0, 0, 0), 4)
                cv.putText(img, text, (25, 465), cv.FONT_HERSHEY_PLAIN,
                        4, (255, 0, 255), 4)
                cv.putText(img, character, (28, 68), cv.FONT_HERSHEY_PLAIN,
                           4, (0, 0, 0), 4)
                cv.putText(img, character, (25, 65), cv.FONT_HERSHEY_PLAIN,
                           4, (0, 255, 255), 4)

            if cv.waitKey(20) &  0xFF==ord('d'):
                break

            screen.fill("black")

            # Scoreboard & Hearts
            for heart in GameObjects.hearts_dict.keys():
                screen.blit(heart, GameObjects.hearts_dict[heart])
            scoreboard_text = pygame.font.Font(None, 100).render("Score\n    " + str(scoreboard.score), True, "white")
            screen.blit(scoreboard_text,(545, 20))
            # Camera - Pygame Integration
            camera_frame = cv2.flip(cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (300, 240)), 1)
            camera_surface = pygame.surfarray.make_surface(np.rot90(camera_frame))
            screen.blit(camera_surface, (0, 0))
            # End Integration Section

            screen.blit(player_surf, (player_pos[0] - 40, player_pos[1] - 40))

            # Spawn new asteroids
            base_time = asteroid_spawner(base_time, time_requirement)
            explosion = False
            # asteroids logic
            temp_asteroids = GameObjects.asteroids.copy()
            i = 0
            for asteroid in temp_asteroids:
                # kill asteroids if word is spelled
                if text.lower() == asteroid.word:
                    GameObjects.asteroids[i].explode()
                    explosion = True
                    i -= 1
                    scoreboard.score += 10 * len(asteroid.word)
                i += 1
            for asteroid in GameObjects.asteroids:
                screen.blit(asteroid.asteroid_surface, asteroid.asteroid_rect)
                screen.blit(asteroid.asteroid_text,
                            (asteroid.asteroid_rect.bottomleft[0] + 10, asteroid.asteroid_rect.bottomleft[1] - 15))
                if asteroid.asteroid_rect.colliderect(player_rect):
                    asteroid.explode()
                    scoreboard.change_hearts(scoreboard.hearts, scoreboard.full_hearts - 1)
                    if scoreboard.full_hearts == 0:
                        running = False
                    continue

                # Calculate new position of asteroid
                dist_x = player_pos.x - asteroid.true_loc[0]
                dist_y = player_pos.y - asteroid.true_loc[1]
                dist_x_abs = abs(dist_x)
                dist_y_abs = abs(dist_y)

                speed_x = dist_x_abs / (dist_y_abs + dist_x_abs) * asteroid.speed
                speed_y = dist_y_abs / (dist_y_abs + dist_x_abs) * asteroid.speed

                if dist_x > 0:
                    asteroid.true_loc[0] += speed_x
                elif dist_x < 0:
                    asteroid.true_loc[0] -= speed_x

                if dist_y > 0:
                    asteroid.true_loc[1] += speed_y
                elif dist_y < 0:
                    asteroid.true_loc[1] -= speed_y

                asteroid.asteroid_rect.centerx = round(asteroid.true_loc[0])
                asteroid.asteroid_rect.centery = round(asteroid.true_loc[1])
            if explosion: text = ""
        else:
            screen.fill("black")
            game_over_text = pygame.font.Font(None, 300).render("GAME OVER", True, "white")
            game_over_rect = game_over_text.get_rect(center=(640, 150))
            screen.blit(game_over_text, game_over_rect)
            screen.blit(scoreboard_text, scoreboard_text.get_rect(center=(640, 350)))
            retry_text = pygame.font.Font(None, 100).render("PRESS SPACE TO RESTART", True, "white")
            screen.blit(retry_text, retry_text.get_rect(center=(640, 500)))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            scoreboard = GameObjects.Scoreboard(health)
            GameObjects.asteroids.clear()
            running = True

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Time in seconds since last frame (60 fps)
    cap.release()
    cv.destroyAllWindows()
