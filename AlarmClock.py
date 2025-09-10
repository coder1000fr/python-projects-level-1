import pygame
import datetime
import time

alarm = 'alarm.mp3'
pygame.mixer.init()
pygame.mixer.music.load(alarm)

timer = input("Enter musice duration: ")
#set_time = pygame.mixer.music.get_busy()

now = datetime.datetime.now()

while now != timer:
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    print(now)
    time.sleep(1)

pygame.mixer.music.play()
time.sleep(10)