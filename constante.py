import pygame

from pygame.locals import *

#Toutes les constantes du programme sont réunis ici pour pouvoir les modifier facilement

#Paramètres de la fenêtre :

largeur_fenetre = 1120
hauteur_fenetre = 640
titre_fenetre = "Time is Monet"
image_icone = "Sprites/icone.png"


#listes des images du jeu :

image_accueil ="Sprites/accueil.jpg"
image_personnage ="Sprites/personnage.jpg"
image_fond1 ="Sprites/background.png"
image_fond2 ="Sprites/background2.png"
image_game_over = "Sprites/gameover.jpg"
image_victoire="Sprites/victoire.png"

#Sprites des personnages

image_personnage1_gauche ="Sprites/Tony_animation/Tony0a.png"
image_personnage1_droite ="Sprites/Tony_animation/Tony0.png"

image_personnage2_gauche ="Sprites/Marius_animation/Marius0a.png"
image_personnage2_droite ="Sprites/Marius_animation/Marius0.png"

image_personnage3_gauche ="Sprites/Cham_animation/Cham0a.png"
image_personnage3_droite ="Sprites/Cham_animation/Cham0.png"

#Animation personnages
index=0
frame_actuelle = 0
temps_animation = 0.5

#personnage 1

image_personnage1_gauche_1 ="Sprites/Tony_animation/Tony1a.png"
image_personnage1_gauche_2 ="Sprites/Tony_animation/Tony2a.png"
image_personnage1_gauche_3 ="Sprites/Tony_animation/Tony3a.png"
image_personnage1_gauche_4 ="Sprites/Tony_animation/Tony4a.png"
image_personnage1_gauche_5 ="Sprites/Tony_animation/Tony5a.png"

image_personnage1_droite_1 ="Sprites/Tony_animation/Tony1.png"
image_personnage1_droite_2 ="Sprites/Tony_animation/Tony2.png"
image_personnage1_droite_3 ="Sprites/Tony_animation/Tony3.png"
image_personnage1_droite_4 ="Sprites/Tony_animation/Tony4.png"
image_personnage1_droite_5 ="Sprites/Tony_animation/Tony5.png"

animation_p1_gauche = [image_personnage1_gauche_1,image_personnage1_gauche_2,image_personnage1_gauche_3,image_personnage1_gauche_4,image_personnage1_gauche_5]
animation_p1_droite =[image_personnage1_droite_1,image_personnage1_droite_2,image_personnage1_droite_3,image_personnage1_droite_4,image_personnage1_droite_5]

#personnage 2

image_personnage2_gauche_1 ="Sprites/Marius_animation/Marius1a.png"
image_personnage2_gauche_2 ="Sprites/Marius_animation/Marius2a.png"
image_personnage2_gauche_3 ="Sprites/Marius_animation/Marius3a.png"
image_personnage2_gauche_4 ="Sprites/Marius_animation/Marius4a.png"
image_personnage2_gauche_5 ="Sprites/Marius_animation/Marius5a.png"

image_personnage2_droite_1 ="Sprites/Marius_animation/Marius1.png"
image_personnage2_droite_2 ="Sprites/Marius_animation/Marius2.png"
image_personnage2_droite_3 ="Sprites/Marius_animation/Marius3.png"
image_personnage2_droite_4 ="Sprites/Marius_animation/Marius4.png"
image_personnage2_droite_5 ="Sprites/Marius_animation/Marius5.png"

animation_p2_gauche = [image_personnage2_gauche_1,image_personnage2_gauche_2,image_personnage2_gauche_3,image_personnage2_gauche_4,image_personnage2_gauche_5]
animation_p2_droite =[image_personnage2_droite_1,image_personnage2_droite_2,image_personnage2_droite_3,image_personnage2_droite_4,image_personnage2_droite_5]

#personnage 3

image_personnage3_gauche_1 ="Sprites/Cham_animation/Cham1a.png"
image_personnage3_gauche_2 ="Sprites/Cham_animation/Cham2a.png"
image_personnage3_gauche_3 ="Sprites/Cham_animation/Cham3a.png"
image_personnage3_gauche_4 ="Sprites/Cham_animation/Cham4a.png"
image_personnage3_gauche_5 ="Sprites/Cham_animation/Cham5a.png"

image_personnage3_droite_1 ="Sprites/Cham_animation/Cham1.png"
image_personnage3_droite_2 ="Sprites/Cham_animation/Cham2.png"
image_personnage3_droite_3 ="Sprites/Cham_animation/Cham3.png"
image_personnage3_droite_4 ="Sprites/Cham_animation/Cham4.png"
image_personnage3_droite_5 ="Sprites/Cham_animation/Cham5.png"

animation_p3_gauche = [image_personnage3_gauche_1,image_personnage3_gauche_2,image_personnage3_gauche_3,image_personnage3_gauche_4,image_personnage3_gauche_5]
animation_p3_droite =[image_personnage3_droite_1,image_personnage3_droite_2,image_personnage3_droite_3,image_personnage3_droite_4,image_personnage3_droite_5]

prepa_droite = "Sprites/prepa droite.png"
prepa_gauche = "Sprites/prepa gauche.png"
collegien_droite ="Sprites/collegien droite.png"
collegien_gauche ="Sprites/collegien gauche.png"


craie1 = "Sprites/craie1.png"
craie2 = "Sprites/craie2.png"
craie2bis = "Sprites/craie2bis.png"
craie3 = "Sprites/craie3.png"
craie4 = "Sprites/craie4.png"
craie5 = "Sprites/craie5.png"
craie5bis = "Sprites/craie5bis.png"
craie6 = "Sprites/craie6.png"

effaceur1 = "Sprites/effaceur1.png"
effaceur2 = "Sprites/effaceur2.png"
effaceur3 = "Sprites/effaceur3.png"
effaceur4 = "Sprites/effaceur4.png"
effaceur5 = "Sprites/effaceur5.png"
effaceur6 = "Sprites/effaceur6.png"
effaceur7 = "Sprites/effaceur7.png"
effaceur8 = "Sprites/effaceur8.png"

livre1 = "Sprites/livre1.png"
livre2 = "Sprites/livre2.png"
livre3 = "Sprites/livre3.png"
livre4 = "Sprites/livre4.png"
livre5 = "Sprites/livre5.png"
livre6 = "Sprites/livre6.png"
livre7 = "Sprites/livre7.png"
livre8 = "Sprites/livre8.png"

feutre1 = "Sprites/feutre1.png"
feutre2 = "Sprites/feutre2.png"
feutre3 = "Sprites/feutre3.png"
feutre4 = "Sprites/feutre4.png"
feutre5 = "Sprites/feutre5.png"
feutre6 = "Sprites/feutre6.png"
feutre7 = "Sprites/feutre7.png"
feutre8 = "Sprites/feutre8.png"

boss = "Sprites/boss.png"


compteur_craie_1 = 0
compteur_craie_2 = 0

#sol

hauteur_sol = 368

#position de départ du personnage
x=200
y=hauteur_sol

#position fond
a=-10
b=0




#position des plateformes
x_plateforme_1 = 725
y_plateforme_1 = 430

x_plateforme_1_ref_niv1 = 737
y_plateforme_1_ref_niv1 = 430

x_plateforme_1_ref_niv2 = 385
y_plateforme_1_ref_niv2 = 472.5


x_plateforme_2 = 787
y_plateforme_2 = 365

x_plateforme_2_ref_niv1 = 787

x_plateforme_2_ref_niv2 = 570



x_plateforme_3 = 2635
y_plateforme_3 = 430

x_plateforme_3_ref_niv1 = 2635

x_plateforme_3_ref_niv2 = 740


x_plateforme_4 = 2685
y_plateforme_4 = 365

x_plateforme_4_ref_niv1 = 2685

x_plateforme_4_ref_niv2 = 930


x_plateforme_5 = 2820
y_plateforme_5 = 215

x_plateforme_5_ref_niv1 = 2820

x_plateforme_5_ref_niv2 = 1102


x_plateforme_6 = 3305
y_plateforme_6 = 365

x_plateforme_6_ref_niv1 = 3305

x_plateforme_6_ref_niv2 = 1280


x_plateforme_7 = 3427
y_plateforme_7 = 425

x_plateforme_7_ref_niv1 = 3427

x_plateforme_7_ref_niv2 = 1450


x_plateforme_8 = 620
y_plateforme_8 = 215

x_plateforme_8_ref_niv1 = 620

x_plateforme_8_ref_niv2 = 1595


x_plateforme_9 = 1875
y_plateforme_9 = 430

x_plateforme_9_ref_niv1 = 1875

x_plateforme_9_ref_niv2 = 1745


x_plateforme_10 = 1050
y_plateforme_10 = 335

x_plateforme_10_ref_niv1 = 1050

x_plateforme_10_ref_niv2 = 1950


x_plateforme_11 = 4040
y_plateforme_11 = 425

x_plateforme_11_ref_niv1 = 4040

x_plateforme_11_ref_niv2 = 2120


x_plateforme_12 = 4095
y_plateforme_12 = 365

x_plateforme_12_ref_niv1 = 4095

x_plateforme_12_ref_niv2 = 2305


x_plateforme_13 = 4360
y_plateforme_13 = 365

x_plateforme_13_ref_niv1 = 4360




x_plateforme_14 = 4640
y_plateforme_14 = 365

x_plateforme_14_ref_niv1 = 4640

x_plateforme_15 = 4838
y_plateforme_15 = 217.5

x_plateforme_15_ref_niv1 = 4838

x_plateforme_16 = 5146
y_plateforme_16 = 217.5

x_plateforme_16_ref_niv1 = 5146

x_plateforme_17 = 5442
y_plateforme_17 = 217.5

x_plateforme_17_ref_niv1 = 5442

x_plateforme_18 = 5725
y_plateforme_18 = 365

x_plateforme_18_ref_niv1 = 5725

x_plateforme_19 = 5850
y_plateforme_19 = 430

x_plateforme_19_ref_niv1 = 5850

x_plateforme_20 = 5960
y_plateforme_20 = 322.5

x_plateforme_20_ref_niv1 = 5960

x_plateforme_21 = 6357
y_plateforme_21 = 322.5

x_plateforme_21_ref_niv1 = 6357

x_plateforme_22 = 9120
y_plateforme_22 = 430

x_plateforme_22_ref_niv1 = 9120

x_plateforme_23 = 9180
y_plateforme_23 = 365

x_plateforme_23_ref_niv1 = 9180

#position des trous (avec y = hauteur du sol)

x_trou_2 = 620
x_trou_1 = 20
x_trou_3 = 2850
x_trou_4 = 1000
x_trou_5 = 4795
x_trou_6 = 6975
x_trou_7 = 7150
x_trou_8 = 7355
x_trou_9 = 7545
x_trou_10 = 7735
x_trou_11 = 8085
x_trou_12 = 8195
x_trou_13 = 8385
x_trou_14 = 8675
x_trou_15 = 8865
x_trou_16 = 9340

x_trou_2_ref = 620
x_trou_1_ref = 20
x_trou_3_ref = 2850
x_trou_4_ref = 1000
x_trou_5_ref = 4795
x_trou_6_ref = 6975
x_trou_7_ref = 7150
x_trou_8_ref = 7355
x_trou_9_ref = 7545
x_trou_10_ref = 7735
x_trou_11_ref = 8085
x_trou_12_ref = 8195
x_trou_13_ref = 8385
x_trou_14_ref = 8675
x_trou_15_ref = 8865
x_trou_16_ref = 9340


x_prepa_1 = 2200
y_prepa_1 = 350

x_prepa_1_ref = 2265

x_prepa_2 = 6750

x_prepa_2_ref = 6750



x_collegien_1 = 4320
y_collegien_1 = 430

x_collegien_1_ref = 4320

x_collegien_2 = 4570

x_collegien_2_ref = 4570

x_collegien_3 = 9820

x_collegien_3_ref = 9820

x_collegien_4 = 10160

x_collegien_4_ref = 10160

x_collegien_5 = 10140

x_collegien_5_ref = 10140



x_craie_1 = 1100
y_craie_1 = 250

x_craie_1_ref = 1100

x_effaceur_1 =1650
y_effaceur_1 = 420

x_effaceur_1_ref =1650

x_craie_2 = 2300
y_craie_2 = 380

x_craie_2_ref = 2300

x_livre_1 = 3100
y_livre_1 = 460

x_livre_1_ref = 3100

x_craie_3 = 3300
y_craie_3 = 250

x_craie_3_ref = 3300

x_feutre_1 = 4200
y_feutre_1 = 380

x_feutre_1_ref = 4200

x_craie_4 = 5300
y_craie_4 = 420

x_craie_4_ref = 5300

x_effaceur_2 =6200
y_effaceur_2 = 250

x_effaceur_2_ref =6200

x_feutre_2 = 6650
y_feutre_2 = 380

x_feutre_2_ref = 6650

x_livre_2 = 7800
y_livre_2 = 460

x_livre_2_ref = 7800

x_craie_5 = 8300
y_craie_5 = 480

x_craie_5_ref = 8300

x_feutre_3 = 8750
y_feutre_3 = 320

x_feutre_3_ref = 8750


x_boss = 2760
y_boss = 280


#sol est un bouleen
sol = 1

gravite = 2.5

#vitesse du personnage
vitesse=1.3


saut = 0  # je m'en sert comme machine à état
max_saut = 180  # en pixel
debut_saut = 0

key = pygame.key.get_pressed

i=0
j=0
k=0

l=0
m=0


def reboot() :
    global a, y, x, hauteur_sol, x_plateforme_2, x_plateforme_4, x_plateforme_3, x_plateforme_5, x_plateforme_6, x_plateforme_7, x_plateforme_8, x_plateforme_9, x_plateforme_10, x_plateforme_11, x_plateforme_12, x_plateforme_13, x_plateforme_14, x_plateforme_15, x_plateforme_16, x_plateforme_17, x_plateforme_18, x_plateforme_19, x_plateforme_20, x_plateforme_21, x_plateforme_22, x_plateforme_23, x_trou_1, x_trou_2, x_trou_3, x_trou_4, x_trou_5, x_trou_6, x_trou_7, x_trou_8, x_trou_9, x_trou_10, x_trou_11, x_trou_12, x_trou_13, x_trou_14, x_trou_15, x_trou_16
    x_plateforme_1 = x_plateforme_1_ref_niv1
    x_plateforme_2 = x_plateforme_2_ref_niv1
    x_plateforme_3 = x_plateforme_3_ref_niv1
    x_plateforme_4 = x_plateforme_4_ref_niv1
    x_plateforme_5 = x_plateforme_5_ref_niv1
    x_plateforme_6 = x_plateforme_6_ref_niv1
    x_plateforme_7 = x_plateforme_7_ref_niv1
    x_plateforme_8 = x_plateforme_8_ref_niv1
    x_plateforme_9 = x_plateforme_9_ref_niv1
    x_plateforme_10 = x_plateforme_10_ref_niv1
    x_plateforme_11 = x_plateforme_11_ref_niv1
    x_plateforme_12 = x_plateforme_12_ref_niv1
    x_plateforme_13 = x_plateforme_13_ref_niv1
    x_plateforme_14 = x_plateforme_14_ref_niv1
    x_plateforme_15 = x_plateforme_15_ref_niv1
    x_plateforme_16 = x_plateforme_16_ref_niv1
    x_plateforme_17 = x_plateforme_17_ref_niv1
    x_plateforme_18 = x_plateforme_18_ref_niv1
    x_plateforme_19 = x_plateforme_19_ref_niv1
    x_plateforme_20 = x_plateforme_20_ref_niv1
    x_plateforme_21 = x_plateforme_21_ref_niv1
    x_plateforme_22 = x_plateforme_22_ref_niv1
    x_plateforme_23 = x_plateforme_23_ref_niv1
    x_trou_1 = x_trou_1_ref
    x_trou_2 = x_trou_2_ref
    x_trou_3 = x_trou_3_ref
    x_trou_4 = x_trou_4_ref
    x_trou_5 = x_trou_5_ref
    x_trou_6 = x_trou_6_ref
    x_trou_7 = x_trou_7_ref
    x_trou_8 = x_trou_8_ref
    x_trou_9 = x_trou_9_ref
    x_trou_10 = x_trou_10_ref
    x_trou_11 = x_trou_11_ref
    x_trou_12 = x_trou_12_ref
    x_trou_13 = x_trou_13_ref
    x_trou_14 = x_trou_14_ref
    x_trou_15 = x_trou_15_ref
    x_trou_16 = x_trou_16_ref
    x = 200
    y = hauteur_sol
    a = -10
    x_prepa_1 = x_prepa_1_ref


#Questions

vieprof=0
vieeleve=0
Q1=1
Q2=0
Q3=0
Q4=0
Q5=0
Q6=0

image_Q1="Sprites/question1.png"
image_Q2="Sprites/question2.png"
image_Q3="Sprites/question3.png"
image_Q4="Sprites/question4.png"
image_Q5="Sprites/question5.png"
image_Q6="Sprites/question6.png"

image_vieprof=["Sprites/vie3.png","Sprites/vie2.png","Sprites/vie1.png","Sprites/vie0.jpg"] #images pour le compteur de vie
image_vieeleve=["Sprites/vie3.png","Sprites/vie2.png","Sprites/vie1.png","Sprites/vie0.jpg"]

#Chrono
temps_max=100
Blanc = (0, 0, 0)
Noir = (255, 255, 255)