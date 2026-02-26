from pynput import keyboard
import numpy as np
import os
import time
import random
import pygame
najboljsi_rezultat = 0
kordinati_kace = [(5, 5), (5, 6), (5, 7)]
smer = "a"
running = True
hrana = (4, 5)
dolzina = 3
pygame.init()
canvas = pygame.display.set_mode((600, 600))
glava = pygame.Rect(30, 30, 60, 200)

color = (240, 50, 70)



def premikanje():
    global kordinati_kace
    global hrana
    global dolzina

    glava = kordinati_kace[0]
    if smer == "t":
        nova_glava = (glava[0] - 1, glava[1])
    elif smer == "g":
        nova_glava = (glava[0] + 1, glava[1])
    elif smer == "f":
        nova_glava = (glava[0], glava[1] - 1)
    elif smer == "h":
        nova_glava = (glava[0], glava[1] + 1)
    else:
        return

    
    kordinati_kace.insert(0, nova_glava)
    if kordinati_kace[0] == hrana:
        r = random.randint(2, 15)
        p = random.randint(2, 15)
        u = r, p
        while u in kordinati_kace:
            r = random.randint(2, 15)
            p = random.randint(2, 15)
            u = r, p
            return u
        hrana = u
        dolzina += 1
    else:
        kordinati_kace.pop()

    
    polja = Polja()
    print(polja)





podvojenost = False




while running:
    
    canvas.fill(color)
    if kordinati_kace[0][0] < 0 or kordinati_kace[0][0] > 15 or kordinati_kace[0][1] < 0 or kordinati_kace[0][1] > 30 or podvojenost == True:
        
        time.sleep(5)
        if dolzina > najboljsi_rezultat:
            najboljsi_rezultat = dolzina
        o = dolzina - 3
        for i in range(o):
            kordinati_kace.pop()
        podvojenost = False
        dolzina = 3
    element = kordinati_kace[0]
    if kordinati_kace.count(element) > 1:
        podvojenost = True
    premikanje()
    
    time.sleep(0.3)
    pygame.draw(canvas, 10, 200, 50, glava)
    
    
    


