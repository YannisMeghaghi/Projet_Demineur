from tkinter import *
from tkinter.messagebox import *
from random import *
from PIL import Image
from PIL import ImageTk as itk
import time
import pygame


Fenetre = Tk()
Largeur = 600
Hauteur = 600
Nombre_ligne = 10
Nombre_colonne = 10
largeur_case = Largeur//Nombre_ligne
hauteur_case = Hauteur//Nombre_colonne
Nombre_bombe = 10
Position_bombe = []
tab_case = ([11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11],[11,11,11,11,11,11,11,11,11,11])



def grille(zone, epaisseur, couleur):
    for i in range (9):
        zone.create_line(0, hauteur_case * (i+1), Largeur, hauteur_case * (i+1), fill = couleur, width = epaisseur)
    for j in range(9):
        zone.create_line(largeur_case * (j+1), 0, largeur_case * (j+1), Hauteur, fill = couleur, width = epaisseur)
    zone.pack()

def affichage():
    for i in range(len(tab_case[0])):
        print()
        for j in range(len(tab_case[1])):
            print(str(tab_case[i][j]) + " ", end = '')
def initialisation_case():
    for i in range (10):
        for j in range (10):
            Zone.create_image( 30 + i*largeur_case, 30 + j*hauteur_case, image = case_image)
            
def initialisation_bombe():
    for i in range(Nombre_bombe):
        tab_case[randint(0,9)][randint(0,9)] = -1

def attribution_valeur(x,y):
    if(tab_case[y][x] != -1):
        if(nombre_voisin(x,y) == 0): #On initialise les cases vides non pas à 0 mais à 11, par la suite on leur donnra la valeur 0
            tab_case[y][x] = 11      #Ce qui perettra de réussir le "efface_enchaine"
        else:
            tab_case[y][x] = nombre_voisin(x,y)

def verification_vitoire():
    compteur = 0
    for i in range(10):
        for j in range (10):
            if(tab_case[y][x] == -1):
                compteur += 1
    if(compteur == 0):
        return true
    else:
        return false

    
def verification_case(x,y):
    if(tab_case[y][x] == -1): #Permet de faire exploser toutes les bombees en même temps
        for i in range (10):
            for j in range (10):
                if(tab_case[j][i] == -1):
                    Zone.create_image(30 + (i*largeur_case), 30 + (j*hauteur_case), image = bombe_image)
                    
        son_countdown.stop()
        son_t_win = pygame.mixer.Sound("t_win.wav")
        son_t_win.play()      
        showinfo("Fin de partie","Oups... Perdu")
        
    else:
        if(tab_case[y][x] == 0 or tab_case[y][x] == 11):
            tab_case[y][x] = 0
            Zone.create_rectangle(x*largeur_case,y*hauteur_case, x*largeur_case + largeur_case, y*hauteur_case + hauteur_case, fill ="#E0E0E0")
            Zone.pack()
        elif(tab_case[y][x] == 1):
            Zone.create_image(30 + (x*largeur_case), 30 + (y*hauteur_case), image = un_image)
            Zone.pack()
        elif(tab_case[y][x] == 2):
            Zone.create_image(30 + (x*largeur_case), 30 + (y*hauteur_case), image = deux_image)
            Zone.pack()
        elif(tab_case[y][x] == 3):
            Zone.create_image(30 + (x*largeur_case), 30 + (y*hauteur_case), image = trois_image)
            Zone.pack()
        elif(tab_case[y][x] == 4):
            Zone.create_image(30 + (x*largeur_case), 30 + (y*hauteur_case), image = quatre_image)
            Zone.pack()
            

def verification_bombe(x,y):#S'appelle verification_bombe mais permet seulement de poser le drapeau
    
    if(tab_case[y][x] == -1):
        tab_case[y][x] = 9
        Zone.create_image(30 + (x*largeur_case), 30 + (y*hauteur_case), image = drapeau_image)
        Zone.pack()
        #affichage()
        print()
    elif(tab_case[y][x] == 9):
        tab_case[y][x] = -1
        Zone.create_image(30 + (x*largeur_case), 30 + (y*hauteur_case), image = case_image)
        Zone.pack()
        #affichage()
        print()
    #else:
     #   pose_drapeau(x,y)
        
def attribution_enchainee():
    for i in range(10):
        for j in range (10):
            attribution_valeur(i,j)
            
def efface_enchaine(x,y):
    if(tab_case[y][x] != 11):
        verification_case(x,y)
    else:
        verification_case(x,y)

        if(x==0 and y==0):#coin haut gauche
            efface_enchaine(x+1,y)
            efface_enchaine(x,y+1)
        elif(x==9 and y == 0):#coin haut droit
            efface_enchaine(x-1,y)
            efface_enchaine(x,y+1)
        elif(x==0 and y == 9):#coin bas gauche
            efface_enchaine(x,y-1)
            efface_enchaine(x+1,y)
        elif(x == 9 and y == 9):#coin bas droit
            efface_enchaine(x-1,y)
            efface_enchaine(x,y-1)
        elif((x!= 0 and x!=9) and y == 0):#ligne du haut
            efface_enchaine(x-1,y)
            efface_enchaine(x+1,y)
            efface_enchaine(x,y+1)
        elif((x!= 0 and x!=9) and y == 9):#ligne du bas
            efface_enchaine(x-1,y)
            efface_enchaine(x+1,y)
            efface_enchaine(x,y-1)
        elif((y!=0 and y != 9) and x == 0):#colonne gauche
            efface_enchaine(x,y-1)
            efface_enchaine(x,y+1)
            efface_enchaine(x+1,y)
        elif((y!=0 and y != 9) and x == 9):#colonne droite
            efface_enchaine(x,y-1)
            efface_enchaine(x,y+1)
            efface_enchaine(x-1,y)
        else:#Position quelconque
            efface_enchaine(x-1,y)
            efface_enchaine(x,y-1)
            efface_enchaine(x+1,y)
            efface_enchaine(x,y+1)
        
    
def clique(event):
    coord_x = event.x//largeur_case
    coord_y = event.y//hauteur_case
    if(tab_case[coord_y][coord_x] != 9):
        if(nombre_voisin(coord_x,coord_y) == 0):
            efface_enchaine(coord_x,coord_y)
        else:
            verification_case(coord_x,coord_y)




def clique_droit(event):
    coord_x = event.x//largeur_case
    coord_y = event.y//hauteur_case
    verification_bombe(coord_x,coord_y)
    
    compteur = 0
    flag = False 
    
    for i in range(10):
        for j in range (10):
            if(tab_case[j][i] == -1):
                compteur += 1
    if(compteur == 0):
        flag = True

    if(flag):
        son_countdown.stop()
        son_ct_win = pygame.mixer.Sound("ct_win.wav")
        son_ct_win.play()
        showinfo("Fin de partie","\tVictoire!\n\nVous avez gagné")



def nombre_voisin(x,y):
    compteur = 0
    if(x == 0 and y == 0):#Si coin supérieur gauche
        for i in range(0,2):
            for j in range(0,2):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
                
    elif(x == 9 and y == 0):#Si coin supérieur droit
        for i in range(-1,1):
            for j in range(0,2):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
                
    elif(x == 0 and y == 9):#Si coin inférieur gauche
        for i in range(0,2):
            for j in range(-1,1):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
                
    elif(x == 9 and y == 9):#Si coin inférieur droit
        for i in range(-1,1):
            for j in range(-1,1):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
                
    elif((x != 0 and x != 9) and y == 0):#Si ligne du haut mais pas coins
        for i in range(-1,2):
            for j in range(0,2):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
                
    elif((x != 0 and x != 9) and y == 9):#Si ligne du bas mais pas coins
        for i in range(-1,2):
            for j in range(-1,1):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
                
    elif(x == 0 and (y != 0 and y != 9)):#Si colonne de gauche mais pas coins
        for i in range(0,2):#Modificaiton ici avant c'était (1,2) mais ca me paraissait bizarre
            for j in range(-1,2):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
                
    elif(x == 9 and (y != 0 and y != 9)):#Si colonne de droite mais pas coins
        for i in range(-1,1):
            for j in range(-1,2):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j)) 
    else:#Si position quelconque
        for i in range(-1,2):
            for j in range(-1,2):
                if(tab_case[y+j][x+i] == -1):
                    compteur += 1
                    #print("Une bombe est située en : ", x+i,y+j)
                #print(str(x+i) + ";" + str(y+j))
        
    
    return compteur



#initialisation_bombe()
#affichage()

if __name__ =="__main__":
    pygame.mixer.init()
    son_bombe_has_been = pygame.mixer.Sound("bomb_has_been.wav")
    son_bombe_has_been.play()
    son_countdown = pygame.mixer.Sound("countdown.wav")
    Couleur = '#E0E0E0'
    Zone =  Canvas(Fenetre, width = Largeur, height = Hauteur, background = Couleur)
    grille(Zone,1,"black")
    Fenetre.bind("<Button-1>",clique)
    Fenetre.bind("<Button-3>",clique_droit)
    case_image = itk.PhotoImage(file = 'Case_Sprite.png')
    drapeau_image = itk.PhotoImage(file = 'Drapeau_Sprite.png')
    un_image = itk.PhotoImage(file = '1_Sprite.png')
    deux_image = itk.PhotoImage(file = '2_Sprite.png')
    trois_image = itk.PhotoImage(file = '3_Sprite.png')
    quatre_image = itk.PhotoImage(file = '4_Sprite.png')
    bombe_image = itk.PhotoImage(file = 'Bombe_Sprite.png')
    initialisation_case()
    initialisation_bombe()
    attribution_enchainee()  
    son_countdown.play()
    #affichage()
    Fenetre.mainloop()
