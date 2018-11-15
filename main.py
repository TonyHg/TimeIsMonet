import pygame, sys, glob

from pygame.locals import *
from constante import *

pygame.mixer.pre_init(44100,16,2,4096)

pygame.init()

#Chrono
police = pygame.font.Font(None, 25)

#Sons
jump_sound = pygame.mixer.Sound("Sons/jumping3.wav")
running_sound = pygame.mixer.Sound("Sons/running2.wav")

#Ouverture de la fenetre Pygame

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

#On defini une icone pour la fenetre

icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

#On definit le titre de la fenetre

pygame.display.set_caption(titre_fenetre)


#Rafraichissement de l'ecran

pygame.display.flip()


Prepa_droite = pygame.image.load(prepa_droite).convert() #Prepa est une surface pygame contenant l'image d'un prepa
Prepa_droite.set_colorkey((255,255,255)) #on enleve le fond blanc

Prepa_gauche = pygame.image.load(prepa_gauche).convert() #Prepa est une surface pygame contenant l'image d'un prepa
Prepa_gauche.set_colorkey((255,255,255)) #on enleve le fond blanc

Collegien_droite = pygame.image.load(collegien_droite).convert()
Collegien_droite.set_colorkey((255,255,255))

Collegien_gauche = pygame.image.load(collegien_gauche).convert()
Collegien_gauche.set_colorkey((255,255,255))

Collegien = Collegien_droite
Collegien2 = Collegien_gauche

Prepa = Prepa_droite


Craie_1 = pygame.image.load(craie1).convert()
Craie_1.set_colorkey((255,255,255))
Craie_2 = pygame.image.load(craie2).convert()
Craie_2.set_colorkey((255,255,255))
Craie_2bis = pygame.image.load(craie2bis).convert()
Craie_2bis.set_colorkey((255,255,255))
Craie_3 = pygame.image.load(craie3).convert()
Craie_3.set_colorkey((255,255,255))
Craie_4 = pygame.image.load(craie4).convert()
Craie_4.set_colorkey((255,255,255))
Craie_5 = pygame.image.load(craie5).convert()
Craie_5.set_colorkey((255,255,255))
Craie_5bis = pygame.image.load(craie5bis).convert()
Craie_5bis.set_colorkey((255,255,255))
Craie_6 = pygame.image.load(craie5).convert()
Craie_6.set_colorkey((255,255,255))

Effaceur1 = pygame.image.load(effaceur1).convert()
Effaceur1.set_colorkey((255,255,255))
Effaceur2 = pygame.image.load(effaceur2).convert()
Effaceur2.set_colorkey((255,255,255))
Effaceur3 = pygame.image.load(effaceur3).convert()
Effaceur3.set_colorkey((255,255,255))
Effaceur4 = pygame.image.load(effaceur4).convert()
Effaceur4.set_colorkey((255,255,255))
Effaceur5 = pygame.image.load(effaceur5).convert()
Effaceur5.set_colorkey((255,255,255))
Effaceur6 = pygame.image.load(effaceur6).convert()
Effaceur6.set_colorkey((255,255,255))
Effaceur7 = pygame.image.load(effaceur7).convert()
Effaceur7.set_colorkey((255,255,255))
Effaceur8 = pygame.image.load(effaceur8).convert()
Effaceur8.set_colorkey((255,255,255))

Livre1 = pygame.image.load(livre1).convert()
Livre1.set_colorkey((255,255,255))
Livre2 = pygame.image.load(livre2).convert()
Livre2.set_colorkey((255,255,255))
Livre3 = pygame.image.load(livre3).convert()
Livre3.set_colorkey((255,255,255))
Livre4 = pygame.image.load(livre4).convert()
Livre4.set_colorkey((255,255,255))
Livre5 = pygame.image.load(livre5).convert()
Livre5.set_colorkey((255,255,255))
Livre6 = pygame.image.load(livre6).convert()
Livre6.set_colorkey((255,255,255))
Livre7 = pygame.image.load(livre7).convert()
Livre7.set_colorkey((255,255,255))
Livre8 = pygame.image.load(livre8).convert()
Livre8.set_colorkey((255,255,255))

Feutre1 = pygame.image.load(feutre1).convert()
Feutre1.set_colorkey((255,255,255))
Feutre2 = pygame.image.load(feutre2).convert()
Feutre2.set_colorkey((255,255,255))
Feutre3 = pygame.image.load(feutre3).convert()
Feutre3.set_colorkey((255,255,255))
Feutre4 = pygame.image.load(feutre4).convert()
Feutre4.set_colorkey((255,255,255))
Feutre5 = pygame.image.load(feutre5).convert()
Feutre5.set_colorkey((255,255,255))
Feutre6 = pygame.image.load(feutre6).convert()
Feutre6.set_colorkey((255,255,255))
Feutre7 = pygame.image.load(feutre7).convert()
Feutre7.set_colorkey((255,255,255))
Feutre8 = pygame.image.load(feutre8).convert()
Feutre8.set_colorkey((255,255,255))


Craie = Craie_1
Effaceur = Effaceur1

animation_craie = [Craie_1,Craie_2,Craie_2bis,Craie_3,Craie_4,Craie_5,Craie_5bis,Craie_6]
animation_effaceur = [Effaceur1, Effaceur2, Effaceur3, Effaceur4, Effaceur5, Effaceur6, Effaceur7, Effaceur8]
animation_livre = [Livre1,Livre2,Livre3,Livre4,Livre5,Livre6,Livre7,Livre8]
animation_feutre = [Feutre1,Feutre2,Feutre3,Feutre4,Feutre5,Feutre6,Feutre7,Feutre8]

Boss = pygame.image.load(boss).convert()
Boss.set_colorkey((255,255,255))

#BOUCLE INFINIE

continuer = 1

pygame.key.set_repeat(100, 10) #pour appuyer longtemps sur une touche

while continuer:

    #On charge la page d'accueil

    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil,(0,0)) # on position l'image d'accueil sur la fenetre

    pygame.display.flip() # on rafraichit la fenetre

    #on remet les variables a 1 a chaque tour
    continuer_accueil = 1
    continuer_personnage = 1
    continuer_jeu = 1
    continuer_jeu2 = 1
    game_over = 1
    victoire=1
    personnage = 0 #variable du choix du personnage


    #BOUCLE POUR l'ACCUEIL
    while continuer_accueil:

		#Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get(): #parmi tous les evenements possibles

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE: #Si l'utilisateur quitter la page ou appuye sur "echap", on change les variables des boucles a 0 pour les arreter

                continuer_accueil = 0
                continuer_personnage = 0
                continuer_jeu = 0
                continuer_jeu2 = 0
                game_over = 0
                victoire=0
                continuer = 0

            elif event.type == KEYDOWN:
                #chargement du 1er niveau
                if event.key == K_RETURN: # appuyer Entrer pour ouvrir le premier niveau
                    continuer_accueil = 0 #on ferme l'accueil

        fond_personnage = pygame.image.load(image_personnage).convert()


    #BOUCLE POUR LE CHOIX DES PERSONNAGES
    while continuer_personnage:

            #Limitation de vitesse de la boucle
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT: #quitter le jeu ferme toutes les boucles
                    continuer_personnage = 0
                    continuer_jeu = 0
                    continuer_jeu2 = 0
                    game_over = 0
                    victoire=0
                    continuer = 0

                elif event.type == KEYDOWN:
                    #Si l'utilisateur presse Echap ici, on revient seulement au menu
                    if event.key == K_ESCAPE:
                        continuer_personnage = 0
                        continuer_jeu = 0
                    if event.key == K_F1: # appuyer F1 pour choisir le 1er personnage et ouvrir le niveau
                        continuer_personnage = 0 #on ferme la fenetre du choix des personnages
                        personnage = "personnage1" #on definit la variable du choix du personnage sur le personnage 1
                    elif event.key == K_F2:
                        continuer_personnage = 0
                        personnage = "personnage2" #Sinon on definit la variable sur le personnage 2
                    elif event.key == K_F3:#Choix du 3e personnage
                        continuer_personnage = 0
                        personnage = "personnage3" #Sinon on definit la variable sur le personnage 3
            fenetre.blit(fond_personnage,(0,0))
            pygame.display.flip()

    if personnage != 0: # on verifie bien que l'utilisateur a choisi un personnage
        fond_jeu = pygame.image.load(image_fond1).convert() #On charge le fond du niveau 1
        chrono = pygame.time.get_ticks() #On demarre le chrono du jeu

        if personnage == "personnage1": #si le personnage 1 a ete choisi, on met les images de celui ci dans les variables du personnage
            perso_gauche = image_personnage1_gauche
            perso_droite = image_personnage1_droite
            animation_gauche = animation_p1_gauche
            animation_droite = animation_p1_droite


        if personnage == "personnage2": #si le personnage 2 a ete choisi, on met les images de celui ci dans les variables du personnage
            perso_gauche = image_personnage2_gauche
            perso_droite = image_personnage2_droite
            animation_gauche = animation_p2_gauche
            animation_droite = animation_p2_droite


        if personnage == "personnage3": #si le personnage 3 a ete choisi, on met les images de celui ci dans les variables du personnage
            perso_gauche = image_personnage3_gauche
            perso_droite = image_personnage3_droite
            animation_gauche = animation_p3_gauche
            animation_droite = animation_p3_droite

        perso = pygame.image.load(perso_droite).convert() #perso est une surface pygame contenant l'image du personnage
        perso.set_colorkey((255,255,255))#enlever le fond blanc
##------------------------------------------------------------------------------
        compteur = 0 #Le compteur pour changer l'image de la liste de l'animation du personnage
        compteur2 = 0 #Le compteur pour changer la vitesse de l'animation
        direction = 1 #Booleen : 1 si le personnage va a droite, sinon 0 si le personnage va gauche

##------------------------------------------------------------------------------


        #music de fond
        pygame.mixer.music.load("Sons/min.wav") #on charge la musique
        pygame.mixer.music.set_volume(0.5) #on regle le volume
        pygame.mixer.music.play(-1) #on lance la musique


        #BOUCLE DU JEU niveau 1
    while continuer_jeu:


            #Limitation de vitesse de la boucle
            pygame.time.Clock().tick(1000)


            if y_prepa_1 - 90 <= y <= hauteur_sol  and x_prepa_1 - 60 <= x <= x_prepa_1 + 64 or y_prepa_1 - 90 <= y <= hauteur_sol  and x_prepa_2 - 60 <= x <= x_prepa_2 + 64 or y_collegien_1 - 90 <= y <= hauteur_sol  and x_collegien_1 - 60 <= x <= x_collegien_1 + 64  or y_collegien_1 - 90 <= y <= hauteur_sol  and x_collegien_2 - 60 <= x <= x_collegien_2 + 55 or y_collegien_1 - 90 <= y <= hauteur_sol  and x_collegien_3 - 60 <= x <= x_collegien_3 + 55 or y_collegien_1 - 90 <= y <= hauteur_sol  and x_collegien_4 - 60 <= x <= x_collegien_4 + 55 or y_collegien_1 - 90 <= y <= hauteur_sol  and x_collegien_5 - 60 <= x <= x_collegien_5 + 55 :   #lorsque le perso touche un prepa, game over

                continuer_jeu = 0
                continuer_jeu2 = 0
                fond_game_over = pygame.image.load(image_game_over).convert()#On charge le fond du game over
                pygame.mixer.music.stop()


            if saut==1:                             #si saut est active et que le personnage n'est pas dans les airs
                sol=0


                if y > debut_saut - max_saut :      #tant qu'il n'atteint pas la hauteur maximale, il monte

                    y-=3


                else :
                    saut=0
                    sol = 1


            elif y == hauteur_sol and x_trou_2 <= x <= x_trou_2 + 80  or y == hauteur_sol and x_trou_1 <= x <= x_trou_1 + 80 or y == hauteur_sol and x_trou_3 <= x <= x_trou_3 + 460 or y == hauteur_sol and x_trou_4 <= x <= x_trou_4 + 420 or y == hauteur_sol and x_trou_5 <= x <= x_trou_5 + 930 or y == hauteur_sol and x_trou_6 <= x <= x_trou_6 + 125 or y == hauteur_sol and x_trou_7 <= x <= x_trou_7 + 140 or y == hauteur_sol and x_trou_7 <= x <= x_trou_7 + 130 or y == hauteur_sol and x_trou_8 <= x <= x_trou_8 + 135 or y == hauteur_sol and x_trou_9 <= x <= x_trou_9 + 130 or y == hauteur_sol and x_trou_10 <= x <= x_trou_10 + 140 or y == hauteur_sol and x_trou_11 <= x <= x_trou_11 + 60 or y == hauteur_sol and x_trou_12 <= x <= x_trou_12 + 140 or y == hauteur_sol and x_trou_13 <= x <= x_trou_13 + 60 or y == hauteur_sol and x_trou_14 <= x <= x_trou_14 + 135 or y == hauteur_sol and x_trou_15 <= x <= x_trou_15 + 145 or y == hauteur_sol and x_trou_16 <= x <= x_trou_16 + 210:             #si le personnage est au niveau d'un trou, il tombe
                sol = 1

            elif y==hauteur_sol :        #si le personnage est sur le sol, il ne tombe pas
                sol = 0

            elif y + 187 == y_plateforme_1 and x_plateforme_1 <= x <= x_plateforme_1 + 83 or y +187 == y_plateforme_2 and x_plateforme_2 <= x <= x_plateforme_2 + 148 or y + 187 == y_plateforme_3 and x_plateforme_3 <= x <= x_plateforme_3 + 83 or y + 187 == y_plateforme_4 and x_plateforme_4 <= x <= x_plateforme_4 + 148 or y + 187 == y_plateforme_7 and x_plateforme_7 <= x <= x_plateforme_7 + 85 or y + 187 == y_plateforme_6 and x_plateforme_6 <= x <= x_plateforme_6 + 148 or y + 187 == y_plateforme_5 and x_plateforme_5 <= x <= x_plateforme_5 + 460 or y + 187 == y_plateforme_8 and x_plateforme_8 <= x <= x_plateforme_8 + 240 or y + 187 == y_plateforme_9 and x_plateforme_9 <= x <= x_plateforme_9 + 340 or y + 187 == y_plateforme_10 and x_plateforme_10 <= x <= x_plateforme_10 + 320 or y + 187 == y_plateforme_11 and x_plateforme_11 <= x <= x_plateforme_11 + 83 or y +187 == y_plateforme_12 and x_plateforme_12 <= x <= x_plateforme_12 + 150 or y +187 == y_plateforme_13 and x_plateforme_13 <= x <= x_plateforme_13 + 150:  #si le personnage est sur une plateforme, il ne tombepas
                sol = 0

            elif y +187 == y_plateforme_14 and x_plateforme_14 <= x <= x_plateforme_14 + 150 or y +187 == y_plateforme_15 and x_plateforme_15 <= x <= x_plateforme_15 + 240 or y +187 == y_plateforme_16 and x_plateforme_16 <= x <= x_plateforme_16 + 240 or y +187 == y_plateforme_17 and x_plateforme_17 <= x <= x_plateforme_17 + 240 or y +187 == y_plateforme_18 and x_plateforme_18 <= x <= x_plateforme_18 + 150 or y +187 == y_plateforme_19 and x_plateforme_19 <= x <= x_plateforme_19 + 83 or y + 187 == y_plateforme_20 and x_plateforme_20 <= x <= x_plateforme_20 + 320 or y + 187 == y_plateforme_21 and x_plateforme_21 <= x <= x_plateforme_21 + 320 or y +187 == y_plateforme_22 and x_plateforme_22 <= x <= x_plateforme_22 + 83 or y +187 == y_plateforme_23 and x_plateforme_23 <= x <= x_plateforme_23 + 150:
                sol = 0

            else :              #sinon, il tombe
                sol=1




            if sol==1 :         #quand sol est egal a 1, le personnage tombe
                y+=gravite




            if y >= hauteur_sol + 200 :         #lorsque le perso tombe dans un trou, game over
                continuer_jeu = 0
                continuer_jeu2 = 0
                fond_game_over = pygame.image.load(image_game_over).convert()#On charge le fond du game over
                pygame.mixer.music.stop() #on arrete la musique



            if 1000<=x<=1120: #si le personnage se trouve a l'arrive
                    continuer_jeu=0 #on ferme le niveau 1
                    x=200 #on repositionne le personnage
                    a=-10 #on repositionne le fond
                    b=0
                    x_plateforme_1 = x_plateforme_1_ref_niv2
                    y_plateforme_1 = y_plateforme_1_ref_niv2
                    x_plateforme_2 = x_plateforme_2_ref_niv2
                    x_plateforme_3 = x_plateforme_3_ref_niv2
                    x_plateforme_4 = x_plateforme_4_ref_niv2
                    x_plateforme_5 = x_plateforme_5_ref_niv2
                    x_plateforme_6 = x_plateforme_6_ref_niv2
                    x_plateforme_7 = x_plateforme_7_ref_niv2
                    x_plateforme_8 = x_plateforme_8_ref_niv2
                    x_plateforme_9 = x_plateforme_9_ref_niv2
                    x_plateforme_10 = x_plateforme_10_ref_niv2
                    x_plateforme_11 = x_plateforme_11_ref_niv2
                    x_plateforme_12 = x_plateforme_12_ref_niv2
                    x_craie_1 = x_craie_1_ref
                    x_craie_2 = x_craie_2_ref
                    x_craie_3 = x_craie_3_ref
                    x_craie_4 = x_craie_4_ref
                    x_craie_5 = x_craie_5_ref
                    x_effaceur_1 = x_effaceur_1_ref
                    x_effaceur_2 = x_effaceur_2_ref
                    x_feutre_1 = x_feutre_1_ref
                    x_feutre_2 = x_feutre_2_ref
                    x_feutre_3 = x_feutre_3_ref
                    x_livre_1 = x_livre_1_ref
                    x_livre_2 = x_livre_2_ref

                    fond_jeu = pygame.image.load(image_fond2).convert()#on charge le fond du niveau 2



            if j == 0 :
                if i < 500 :
                    x_prepa_1 += 0.3
                    x_prepa_2 += 0.3
                    x_collegien_1 += 0.5
                    x_collegien_2 -= 0.5
                    x_collegien_3 += 0.5
                    x_collegien_4 -= 0.5
                    x_collegien_5 += 0.5
                    i+=1
                    Prepa = Prepa_droite
                    Collegien = Collegien_droite
                    Collegien2 = Collegien_gauche


                else :
                    j=1

            if j == 1 :
                if i > 0 :
                    x_prepa_1 -= 0.3
                    x_prepa_2 -= 0.3
                    x_collegien_1 -= 0.5
                    x_collegien_2 += 0.5
                    x_collegien_3 -= 0.5
                    x_collegien_4 += 0.5
                    x_collegien_5 -= 0.5
                    i-=1
                    Prepa = Prepa_gauche
                    Collegien2 = Collegien_droite
                    Collegien = Collegien_gauche

                else :
                    j = 0






            for event in pygame.event.get():
                if event.type == QUIT: #Quitter le jeu ferme toutes les boucles
                    continuer_jeu = 0
                    continuer_jeu2 = 0
                    continuer = 0
                    game_over = 0
                    victoire=0
                    pygame.mixer.music.stop() #on arrete la musique

##------------------------------------------------------------------------------
                elif event.type == KEYUP: #KEYUP = touches pas pressees
                    if direction == 0: #si le personnage va a gauche
                        perso = pygame.image.load(perso_gauche).convert() #on charge l'image du personnage immobile regardant a gauche
                    else: # sinon il va vers la droite
                        perso = pygame.image.load(perso_droite).convert() #on charge l'image du personnage immobile regardant a droite
                    perso.set_colorkey((255,255,255))

##------------------------------------------------------------------------------

                elif event.type == KEYDOWN:



                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                    if pygame.key.get_pressed()[pygame.K_ESCAPE] :
                        continuer_personnage = 0
                        continuer_jeu = 0
                        continuer_jeu2 = 0
                        game_over = 0
                        victoire=0
                        pygame.mixer.music.stop() #on arrete la musique


                #Touche de deplacement du personnage

            if pygame.key.get_pressed()[pygame.K_RIGHT]: #Si fleche droite"

                #perso = pygame.image.load(perso_droite).convert()
                #perso.set_colorkey((255,255,255))

##------------------------------------------------------------------------------
                perso = pygame.image.load(animation_droite[compteur]).convert() #on charge l'animation
                perso.set_colorkey((255,255,255))
                if (compteur2 % 30 == 0): #changer la vitesse de l'animation
                    compteur = (compteur + 1) % len(animation_droite) # faire defiler l'indice des images de la liste
                compteur2 = compteur2 + 1 #on incremente le compteur
                direction = 1 #le personnage va a droite
##------------------------------------------------------------------------------


                if x>=650:      #Si le perso arrive a 650 pixels, il est immobile et le fond, ainsi que les plateformes defilent vers la gauche


                    if a <= -9880 :
                        if x >= largeur_fenetre - vitesse -50 :  #on s'assure que le perso ne puisse pas sortir de la fenetre
                            x=largeur_fenetre -50


                        else :
                            x+=vitesse
                    else :
                        a-=vitesse
                        x_plateforme_1-=vitesse
                        x_plateforme_2-=vitesse
                        x_plateforme_3-=vitesse
                        x_plateforme_4-=vitesse
                        x_plateforme_5-=vitesse
                        x_plateforme_6-=vitesse
                        x_plateforme_7-=vitesse
                        x_plateforme_8-=vitesse
                        x_plateforme_9-=vitesse
                        x_plateforme_10-=vitesse
                        x_plateforme_11-=vitesse
                        x_plateforme_12-=vitesse
                        x_plateforme_13-=vitesse
                        x_plateforme_14-=vitesse
                        x_plateforme_15-=vitesse
                        x_plateforme_16-=vitesse
                        x_plateforme_17-=vitesse
                        x_plateforme_18-=vitesse
                        x_plateforme_19-=vitesse
                        x_plateforme_20-=vitesse
                        x_plateforme_21-=vitesse
                        x_plateforme_22-=vitesse
                        x_plateforme_23-=vitesse
                        x_trou_2-=vitesse
                        x_trou_1-=vitesse
                        x_trou_3-=vitesse
                        x_trou_4-=vitesse
                        x_trou_5-=vitesse
                        x_trou_6-=vitesse
                        x_trou_7-=vitesse
                        x_trou_8-=vitesse
                        x_trou_9-=vitesse
                        x_trou_10-=vitesse
                        x_trou_11-=vitesse
                        x_trou_12-=vitesse
                        x_trou_13-=vitesse
                        x_trou_14-=vitesse
                        x_trou_15-=vitesse
                        x_trou_16-=vitesse
                        x_prepa_1-=vitesse
                        x_prepa_2-=vitesse
                        x_collegien_1-=vitesse
                        x_collegien_2-=vitesse
                        x_collegien_3-=vitesse
                        x_collegien_4-=vitesse
                        x_collegien_5-=vitesse




                else :          #Sinon, il avance vers la droite
                    x+=vitesse





            if pygame.key.get_pressed()[K_UP]:

                if sol == 0 :

                            if not saut:  # pour pas sauter 4-5 fois en l'air
                                saut = 1
                                debut_saut = y
                                pygame.mixer.Sound.play(jump_sound)



            if pygame.key.get_pressed()[pygame.K_LEFT]: #Si "fleche gauche"

##------------------------------------------------------------------------------
                perso = pygame.image.load(animation_gauche[compteur]).convert() #on charge l'animation
                perso.set_colorkey((255,255,255))
                if (compteur2 % 30 == 0): #changer la vitesse de l'animation
                    compteur = (compteur + 1) % len(animation_gauche) # faire defiler l'indice des images de la liste
                compteur2 = compteur2 + 1 #on incremente le compteur
                direction = 0 #le personnage va a gauche
##------------------------------------------------------------------------------



                if x<=400:

                    if a >= -vitesse :
                        if x <=vitesse :
                            x=0
                        else :
                            x-=vitesse

                    else :
                            a+=vitesse
                            x_plateforme_1+=vitesse
                            x_plateforme_2+=vitesse
                            x_plateforme_3+=vitesse
                            x_plateforme_4+=vitesse
                            x_plateforme_5+=vitesse
                            x_plateforme_6+=vitesse
                            x_plateforme_7+=vitesse
                            x_plateforme_8+=vitesse
                            x_plateforme_9+=vitesse
                            x_plateforme_10+=vitesse
                            x_plateforme_11+=vitesse
                            x_plateforme_12+=vitesse
                            x_plateforme_13+=vitesse
                            x_plateforme_14+=vitesse
                            x_plateforme_15+=vitesse
                            x_plateforme_16+=vitesse
                            x_plateforme_17+=vitesse
                            x_plateforme_18+=vitesse
                            x_plateforme_19+=vitesse
                            x_plateforme_20+=vitesse
                            x_plateforme_21+=vitesse
                            x_plateforme_22+=vitesse
                            x_plateforme_23+=vitesse
                            x_trou_2+=vitesse
                            x_trou_1+=vitesse
                            x_trou_3+=vitesse
                            x_trou_4+=vitesse
                            x_trou_5+=vitesse
                            x_trou_6+=vitesse
                            x_trou_7+=vitesse
                            x_trou_8+=vitesse
                            x_trou_9+=vitesse
                            x_trou_10+=vitesse
                            x_trou_11+=vitesse
                            x_trou_12+=vitesse
                            x_trou_13+=vitesse
                            x_trou_14+=vitesse
                            x_trou_15+=vitesse
                            x_trou_16+=vitesse
                            x_prepa_1+=vitesse
                            x_prepa_2+=vitesse
                            x_collegien_1+=vitesse
                            x_collegien_2+=vitesse
                            x_collegien_3+=vitesse
                            x_collegien_4+=vitesse
                            x_collegien_5+=vitesse

                else :          #Sinon, il avance vers la gauche
                    x-=vitesse




            #On raffraichi la fenetre, pour afficher les nouvelles positions du personnage et du fond
            fenetre.blit(fond_jeu,(a,b))
            fenetre.blit(perso,(x,y))
            fenetre.blit(Prepa,(x_prepa_1,y_prepa_1))
            fenetre.blit(Prepa,(x_prepa_2,y_prepa_1))
            fenetre.blit(Collegien,(x_collegien_1,y_collegien_1))
            fenetre.blit(Collegien2,(x_collegien_2,y_collegien_1))
            fenetre.blit(Collegien,(x_collegien_3,y_collegien_1))
            fenetre.blit(Collegien2,(x_collegien_4,y_collegien_1))
            fenetre.blit(Collegien,(x_collegien_5,y_collegien_1))




            secondes = (pygame.time.get_ticks()-chrono)/1000 #On compte le chrono en seconde
            temps_restant = temps_max-int(secondes)
            texte = "Temps restant: {0}".format(temps_restant)
            affichage = police.render(texte, True, Noir)
            fenetre.blit(affichage, [10, 10])
            if secondes > temps_max: #Si le chrono depasse le temps limite, on ferme les boucles de jeu, ce qui ouvre la boucle game over
                continuer_jeu = 0
                continuer_jeu2 = 0
                fond_game_over = pygame.image.load(image_game_over).convert()#On charge le fond du game over
                pygame.mixer.music.stop()


            pygame.display.flip()


    #music de fond
    pygame.mixer.music.load("Sons/2min.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)



##------------------------------------------------------------------------------

    #BOUCLE NIVEAU 2

    while continuer_jeu2:
            pygame.time.Clock().tick(1000) #Limitation de vitesse de la boucle
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer_accueil = 0
                    continuer_personnage = 0
                    continuer_jeu = 0
                    continuer_jeu2 = 0
                    game_over = 0
                    victoire=0
                    continuer = 0
##------------------------------------------------------------------------------
                elif event.type == KEYUP: #KEYUP = touches pas pressees
                    if direction == 0: #si le personnage va a gauche
                        perso = pygame.image.load(perso_gauche).convert() #on charge l'image du personnage immobile regardant a gauche
                    else: # sinon il va vers la droite
                        perso = pygame.image.load(perso_droite).convert() #on charge l'image du personnage immobile regardant a droite
                    perso.set_colorkey((255,255,255))
##------------------------------------------------------------------------------
            if pygame.key.get_pressed()[pygame.K_ESCAPE] :#Si l'utilisateur presse Echap ici, on revient seulement au menu
                        continuer_personnage = 0
                        continuer_jeu = 0
                        continuer_jeu2 = 0
                        game_over=0
                        victoire=0


            if  y_effaceur_1 - 90 <= y <= y_effaceur_1 + 40 and x_effaceur_1 - 63 <= x <= x_effaceur_1 + 48 or y_craie_1 - 90 <= y <= y_craie_1 + 40 and x_craie_1 - 63 <= x <= x_craie_1 + 48 or y_craie_2 - 90 <= y <= y_craie_2 + 40 and x_craie_2 - 63 <= x <= x_craie_2 + 48 or y_effaceur_1 - 90 <= y <= y_effaceur_1 + 48 and x_effaceur_1 - 63 <= x <= x_effaceur_1 + 48 or y_effaceur_2 - 90 <= y <= y_effaceur_2 + 40 and x_effaceur_2 - 63 <= x <= x_effaceur_2 + 48 or y_craie_3 - 90 <= y <= y_craie_3 + 40 and x_craie_3 - 63 <= x <= x_craie_3 + 48 or y_craie_4 - 90 <= y <= y_craie_4 + 40 and x_craie_4 - 63 <= x <= x_craie_4 + 48 or y_craie_5 - 90 <= y <= y_craie_5 + 40 and x_craie_5 - 63 <= x <= x_craie_5 + 48 or y_feutre_1 - 90 <= y <= y_feutre_1 + 40 and x_feutre_1 - 63 <= x <= x_feutre_1 + 48 or y_feutre_2 - 90 <= y <= y_feutre_2 + 40 and x_feutre_2 - 63 <= x <= x_feutre_2 + 48 or y_feutre_3 - 90 <= y <= y_feutre_3 + 40 and x_feutre_3 - 63 <= x <= x_feutre_3 + 48:   #lorsque le perso touche une craie game over

                continuer_jeu = 0
                continuer_jeu2 = 0
                fond_game_over = pygame.image.load(image_game_over).convert()#On charge le fond du game over
                pygame.mixer.music.stop()

            elif y_livre_1 - 90 <= y <= y_livre_1 + 40 and x_livre_1 - 63 <= x <= x_livre_1 + 48 or y_livre_2 - 90 <= y <= y_livre_2 + 40 and x_livre_2 - 63 <= x <= x_livre_2 + 48 :

                continuer_jeu = 0
                continuer_jeu2 = 0
                fond_game_over = pygame.image.load(image_game_over).convert()#On charge le fond du game over
                pygame.mixer.music.stop()



            if saut==1:                             #si saut est active et que le personnage n'est pas dans les airs
                sol=0

                if y > debut_saut - max_saut :      #tant qu'il n'atteint pas la hauteur maximale, il monte

                    y-=3

                else :
                    saut=0
                    sol = 1


            elif y==hauteur_sol :      #si le personnage est sur le sol, il ne tombe pas
                sol = 0

            elif y + 187 == y_plateforme_1 and x_plateforme_1 <= x <= x_plateforme_1 + 95 or y + 187 == y_plateforme_1 and x_plateforme_2 <= x <= x_plateforme_2 + 95 or y + 187 == y_plateforme_1 and x_plateforme_3 <= x <= x_plateforme_3 + 95 or y + 187 == y_plateforme_1 and x_plateforme_4 <= x <= x_plateforme_4 + 95 or y + 187 == y_plateforme_1 and x_plateforme_7 <= x <= x_plateforme_7 + 95 or y + 187 == y_plateforme_1 and x_plateforme_5 <= x <= x_plateforme_5 + 95 or y + 187 == y_plateforme_1 and x_plateforme_6 <= x <= x_plateforme_6 + 95 or y + 187 == y_plateforme_1 and x_plateforme_8 <= x <= x_plateforme_8 + 95 or y + 187 == y_plateforme_1 and x_plateforme_9 <= x <= x_plateforme_9 + 95 or y + 187 == y_plateforme_1 and x_plateforme_10 <= x <= x_plateforme_10 + 95 or y + 187 == y_plateforme_1 and x_plateforme_11 <= x <= x_plateforme_11 + 95 or y + 187 == y_plateforme_1 and x_plateforme_12 <= x <= x_plateforme_12 + 95:
                sol = 0



            else :              #sinon, il tombe
                sol=1



            if sol==1 :         #quand sol est egal a 1, le personnage tombe
                y+=gravite



            x_craie_1 -= 1.5
            x_craie_2 -= 1.5
            x_craie_3 -= 1.5
            x_craie_4 -= 1.5
            x_craie_5 -= 1.5
            x_effaceur_1 -= 1.5
            x_effaceur_2 -= 1.5
            x_livre_1 -= 1.5
            x_livre_2 -= 1.5
            x_feutre_1 -= 1.5
            x_feutre_2 -= 1.5
            x_feutre_3 -= 1.5


            if l % 10000  == 1 :
                l=0
                if m == 0 :
                    m=1
                    y_boss -= 10
                elif m == 1 :
                    m=0
                    y_boss += 10
            else :
                l+=1




            Craie = animation_craie[compteur_craie_1] #on charge l'animation
            Effaceur = animation_effaceur[compteur_craie_1]
            Livre = animation_livre[compteur_craie_1]
            Feutre = animation_feutre[compteur_craie_1]
            if (compteur_craie_2 % 60 == 0): #changer la vitesse de l'animation
                compteur_craie_1 = (compteur_craie_1 + 1) % len(animation_craie) # faire defiler l'indice des images de la liste
            compteur_craie_2 = compteur_craie_2 + 1 #on incremente le compteur




            if pygame.key.get_pressed()[pygame.K_RIGHT]: #Si fleche droite"

##------------------------------------------------------------------------------
                perso = pygame.image.load(animation_droite[compteur]).convert() #on charge l'animation
                perso.set_colorkey((255,255,255))
                if (compteur2 % 30 == 0): #changer la vitesse de l'animation
                    compteur = (compteur + 1) % len(animation_droite) # faire defiler l'indice des images de la liste
                compteur2 = compteur2 + 1 #on incremente le compteur
                direction = 1 #le personnage va a droite
##------------------------------------------------------------------------------


                if x>=650:      #Si le perso arrive a 650 pixels, il est immobile et le fond, ainsi que les plateformes defilent vers la gauche

                    if a <= -1850 :
                        if x >= largeur_fenetre - vitesse -50 :  #on s'assure que le perso ne puisse pas sortir de la fenetre
                            x=largeur_fenetre -50


                        else :
                            x+=vitesse

                    else :
                        a-=vitesse
                        x_plateforme_1-=vitesse
                        x_plateforme_2-=vitesse
                        x_plateforme_3-=vitesse
                        x_plateforme_4-=vitesse
                        x_plateforme_5-=vitesse
                        x_plateforme_6-=vitesse
                        x_plateforme_7-=vitesse
                        x_plateforme_8-=vitesse
                        x_plateforme_9-=vitesse
                        x_plateforme_10-=vitesse
                        x_plateforme_11-=vitesse
                        x_plateforme_12-=vitesse
                        x_craie_1-=vitesse
                        x_craie_2-=vitesse
                        x_craie_3-=vitesse
                        x_craie_4-=vitesse
                        x_craie_5-=vitesse
                        x_effaceur_1-=vitesse
                        x_effaceur_2-=vitesse
                        x_livre_1-=vitesse
                        x_livre_2-=vitesse
                        x_feutre_1-=vitesse
                        x_feutre_2-=vitesse
                        x_feutre_3-=vitesse
                        x_boss-=vitesse


                else :  #Sinon, il avance vers la droite
                    x+=vitesse

                if 750<=x<=1120: #le personnage arrive au niveau du boss -> QCM
                    question = 1
                    while question: #BOUCLE QUESTION
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        continuer_accueil = 0
                                        continuer_personnage = 0
                                        continuer_jeu = 0
                                        continuer_jeu2 = 0
                                        game_over = 0
                                        victoire=0
                                        continuer = 0
                                        question = 0

                                pygame.time.Clock().tick(30)
                                while Q1: #Question 1
                                        pygame.time.Clock().tick(30)
                                        Question1=pygame.image.load(image_Q1).convert()
                                        ViesProf=pygame.image.load(image_vieprof[vieprof]).convert()
                                        ViesEleve=pygame.image.load(image_vieeleve[vieeleve]).convert()
                                        fenetre.blit(Question1,(50,50)) # on position l'image sur la fenetre
                                        fenetre.blit(ViesProf,(900,100)) # on position l'image sur la fenetre
                                        fenetre.blit(ViesEleve,(100,100)) # on position l'image sur la fenetre
                                        pygame.display.flip()

                                    #if event.type == KEYDOWN:
                                        event=pygame.event.wait() #on attend qu'une action soit lancee
                                        if event.type == QUIT:
                                            continuer_accueil = 0
                                            continuer_personnage = 0
                                            continuer_jeu = 0
                                            continuer_jeu2 = 0
                                            game_over = 0
                                            victoire=0
                                            continuer = 0
                                            question = 0
                                            Q1 = 0
                                        if pygame.key.get_pressed()[pygame.K_F3]: #Joueur appuye sur la bonne reponse -> vie du boss -1
                                            if vieprof<2 and vieeleve <2:
                                                vieprof=vieprof+1 #Vie du boss decend de 1
                                                Q1=0 #on ferme la question 1 et on ouvre la question 2
                                                Q2=1
                                        if pygame.key.get_pressed()[pygame.K_F1] or pygame.key.get_pressed()[pygame.K_F2] or pygame.key.get_pressed()[pygame.K_F4] : #Joueur choisi la mauvaise reponse
                                            if vieprof<2 and vieeleve <2:
                                                vieeleve=vieeleve+1 #joueur perd une vie
                                                Q1=0 #on ferme la question 1 et on ouvre la question 2
                                                Q2=1

                                        pygame.display.flip()

                                while Q2: #Question 2
                                    Question2=pygame.image.load(image_Q2).convert() # on charge la deuxieme question
                                    fenetre.blit(Question2,(50,50)) # on position l'image sur la fenetre
                                    ViesProf=pygame.image.load(image_vieprof[vieprof]).convert()
                                    ViesEleve=pygame.image.load(image_vieeleve[vieeleve]).convert()
                                    fenetre.blit(ViesProf,(900,100)) # on position l'image sur la fenetre
                                    fenetre.blit(ViesEleve,(100,100)) # on position l'image sur la fenetre

                                    event=pygame.event.wait()
                                    if event.type == QUIT:
                                            continuer_accueil = 0
                                            continuer_personnage = 0
                                            continuer_jeu = 0
                                            continuer_jeu2 = 0
                                            game_over = 0
                                            victoire=0
                                            continuer = 0
                                            question = 0
                                            Q2 = 0
                                    if pygame.key.get_pressed()[pygame.K_F3]: #Joueur appuye sur la bonne reponse -> vie du boss -1
                                        if vieprof<2 and vieeleve <2:
                                            vieprof=vieprof+1 #Vie du boss decend de 1
                                            Q2=0
                                            Q3=1
                                    if pygame.key.get_pressed()[pygame.K_F1] or pygame.key.get_pressed()[pygame.K_F2] or pygame.key.get_pressed()[pygame.K_F4] : #Joueur choisi la mauvaise reponse
                                        if vieprof<2 and vieeleve <2:
                                            vieeleve=vieeleve+1 #joueur perd une vie
                                            Q2=0
                                            Q3=1
                                    pygame.display.flip()

                                while Q3: #Question 3
                                    Question3=pygame.image.load(image_Q3).convert() # on charge la 3 question
                                    fenetre.blit(Question3,(50,50)) # on position l'image sur la fenetre
                                    ViesProf=pygame.image.load(image_vieprof[vieprof]).convert()
                                    ViesEleve=pygame.image.load(image_vieeleve[vieeleve]).convert()
                                    fenetre.blit(ViesProf,(900,100)) # on position l'image sur la fenetre
                                    fenetre.blit(ViesEleve,(100,100)) # on position l'image sur la fenetre

                                    event=pygame.event.wait()
                                    if event.type == QUIT:
                                            continuer_accueil = 0
                                            continuer_personnage = 0
                                            continuer_jeu = 0
                                            continuer_jeu2 = 0
                                            game_over = 0
                                            victoire=0
                                            continuer = 0
                                            question = 0
                                            Q3 = 0
                                    if pygame.key.get_pressed()[pygame.K_F1]:
                                        if vieprof<2 and vieeleve <3:
                                                vieprof=vieprof+1 #Vie du boss decend de 1
                                                Q3=0
                                                Q4=1
                                        if vieprof==2: #Boss n'a plus de vie, victoire !
                                            Q3=0
                                            question=0
                                            continuer_jeu2=0
                                            game_over=0
                                    elif pygame.key.get_pressed()[pygame.K_F3] or pygame.key.get_pressed()[pygame.K_F2] or pygame.key.get_pressed()[pygame.K_F4] : #Joueur choisi la mauvaise reponse
                                        if vieprof<3 and vieeleve <2:
                                                vieeleve=vieeleve+1 #joueur perd une vie
                                                Q3=0
                                                Q4=1
                                        if vieeleve==2: #eleve n'a plus de vie, game over !
                                            Q3=0
                                            question=0
                                            continuer_jeu2=0
                                            victoire=0
                                    pygame.display.flip()

                                while Q4: #Question 4
                                    Question4=pygame.image.load(image_Q4).convert() # on charge la 4 question
                                    fenetre.blit(Question4,(50,50)) # on position l'image sur la fenetre
                                    ViesProf=pygame.image.load(image_vieprof[vieprof]).convert()
                                    ViesEleve=pygame.image.load(image_vieeleve[vieeleve]).convert()
                                    fenetre.blit(ViesProf,(900,100)) # on position l'image sur la fenetre
                                    fenetre.blit(ViesEleve,(100,100)) # on position l'image sur la fenetre

                                    event=pygame.event.wait()
                                    if event.type == QUIT:
                                            continuer_accueil = 0
                                            continuer_personnage = 0
                                            continuer_jeu = 0
                                            continuer_jeu2 = 0
                                            game_over = 0
                                            victoire=0
                                            continuer = 0
                                            question = 0
                                            Q4 = 0
                                    if pygame.key.get_pressed()[pygame.K_F4]:
                                        if vieprof<2 and vieeleve <3:
                                                vieprof=vieprof+1 #Vie du boss decend de 1
                                                Q4=0
                                                Q5=1
                                        if vieprof==2: #Boss n'a plus de vie, victoire !
                                            Q4=0
                                            question=0
                                            continuer_jeu2=0
                                            game_over=0
                                    elif pygame.key.get_pressed()[pygame.K_F1] or pygame.key.get_pressed()[pygame.K_F2] or pygame.key.get_pressed()[pygame.K_F3] : #Joueur choisi la mauvaise reponse
                                        if vieprof<3 and vieeleve <2:
                                                vieeleve=vieeleve+1 #joueur perd une vie
                                                Q4=0
                                                Q5=1
                                        if vieeleve==2: #eleve n'a plus de vie, game over !
                                            Q4=0
                                            question=0
                                            continuer_jeu2=0
                                            victoire=0
                                    pygame.display.flip()

                                while Q5: #Question 5
                                    Question5=pygame.image.load(image_Q5).convert() # on charge la 5 question
                                    fenetre.blit(Question5,(50,50)) # on position l'image sur la fenetre
                                    ViesProf=pygame.image.load(image_vieprof[vieprof]).convert()
                                    ViesEleve=pygame.image.load(image_vieeleve[vieeleve]).convert()
                                    fenetre.blit(ViesProf,(900,100)) # on position l'image sur la fenetre
                                    fenetre.blit(ViesEleve,(100,100)) # on position l'image sur la fenetre

                                    event=pygame.event.wait()
                                    if event.type == QUIT:
                                            continuer_accueil = 0
                                            continuer_personnage = 0
                                            continuer_jeu = 0
                                            continuer_jeu2 = 0
                                            game_over = 0
                                            victoire=0
                                            continuer = 0
                                            question = 0
                                            Q5 = 0
                                    if pygame.key.get_pressed()[pygame.K_F3]:
                                        if vieprof<2 and vieeleve <3:
                                                vieprof=vieprof+1 #Vie du boss decend de 1
                                                Q5=0
                                                Q6=1
                                        if vieprof==2: #Boss n'a plus de vie, victoire !
                                            Q3=0
                                            question=0
                                            continuer_jeu2=0
                                            game_over=0
                                    elif pygame.key.get_pressed()[pygame.K_F1] or pygame.key.get_pressed()[pygame.K_F2] or pygame.key.get_pressed()[pygame.K_F3] : #Joueur choisi la mauvaise reponse
                                        if vieprof<3 and vieeleve <2:
                                                vieeleve=vieeleve+1 #joueur perd une vie
                                                Q5=0
                                                Q6=1
                                        if vieeleve==2: #eleve n'a plus de vie, game over !
                                            Q5=0
                                            question=0
                                            continuer_jeu2=0
                                            victoire=0
                                    pygame.display.flip()

                                while Q6: #Question 6
                                    Question6=pygame.image.load(image_Q6).convert() # on charge la 6 question
                                    fenetre.blit(Question6,(50,50)) # on position l'image sur la fenetre
                                    ViesProf=pygame.image.load(image_vieprof[vieprof]).convert()
                                    ViesEleve=pygame.image.load(image_vieeleve[vieeleve]).convert()
                                    fenetre.blit(ViesProf,(900,100)) # on position l'image sur la fenetre
                                    fenetre.blit(ViesEleve,(100,100)) # on position l'image sur la fenetre

                                    event=pygame.event.wait()
                                    if event.type == QUIT:
                                            continuer_accueil = 0
                                            continuer_personnage = 0
                                            continuer_jeu = 0
                                            continuer_jeu2 = 0
                                            game_over = 0
                                            victoire=0
                                            continuer = 0
                                            question = 0
                                            Q6 = 0
                                    if pygame.key.get_pressed()[pygame.K_F1]:
                                        if vieprof<2 and vieeleve <3:
                                                vieprof=vieprof+1 #Vie du boss decend de 1
                                        if vieprof==2: #Boss n'a plus de vie, victoire !
                                            Q3=0
                                            question=0
                                            continuer_jeu2=0
                                            game_over=0
                                    elif pygame.key.get_pressed()[pygame.K_F3] or pygame.key.get_pressed()[pygame.K_F2] or pygame.key.get_pressed()[pygame.K_F4] : #Joueur choisi la mauvaise reponse
                                        if vieprof<3 and vieeleve <2:
                                                vieeleve=vieeleve+1 #joueur perd une vie
                                                Q6=0
                                        if vieeleve==2: #eleve n'a plus de vie, game over !
                                            Q6=0
                                            question=0
                                            continuer_jeu2=0
                                            victoire=0
                                    pygame.display.flip()

            if pygame.key.get_pressed()[K_UP]: #Sauter

                if sol == 0 :

                            if not saut:  # pour pas sauter 4-5 fois en l'air
                                saut = 1
                                debut_saut = y


            if pygame.key.get_pressed()[pygame.K_LEFT]: #Si "fleche gauche"

##------------------------------------------------------------------------------
                perso = pygame.image.load(animation_gauche[compteur]).convert() #on charge l'animation
                perso.set_colorkey((255,255,255))
                if (compteur2 % 30 == 0): #changer la vitesse de l'animation
                    compteur = (compteur + 1) % len(animation_gauche) # faire defiler l'indice des images de la liste
                compteur2 = compteur2 + 1 #on incremente le compteur
                direction = 0 #le personnage va a gauche
##------------------------------------------------------------------------------



                if x<=400:

                    if a >= -vitesse :
                        if x <=vitesse :
                            x=0
                        else :
                            x-=vitesse


                    else :
                            a+=vitesse
                            x_plateforme_1+=vitesse
                            x_plateforme_2+=vitesse
                            x_plateforme_3+=vitesse
                            x_plateforme_4+=vitesse
                            x_plateforme_5+=vitesse
                            x_plateforme_6+=vitesse
                            x_plateforme_7+=vitesse
                            x_plateforme_8+=vitesse
                            x_plateforme_9+=vitesse
                            x_plateforme_10+=vitesse
                            x_plateforme_11+=vitesse
                            x_plateforme_12+=vitesse
                            x_craie_1+=vitesse
                            x_craie_2+=vitesse
                            x_craie_3+=vitesse
                            x_craie_4+=vitesse
                            x_craie_5+=vitesse
                            x_effaceur_1+=vitesse
                            x_effaceur_2+=vitesse
                            x_livre_1+=vitesse
                            x_livre_2+=vitesse
                            x_feutre_1+=vitesse
                            x_feutre_2+=vitesse
                            x_feutre_3+=vitesse
                            x_boss+=vitesse



                else :          #Sinon, il avance vers la gauche
                    x-=vitesse


            #On raffraichi la fenetre, pour afficher les nouvelles positions du personnage et du fond
            fenetre.blit(fond_jeu,(a,b))
            fenetre.blit(perso,(x,y))
            fenetre.blit(Craie,(x_craie_1,y_craie_1))
            fenetre.blit(Craie,(x_craie_2,y_craie_2))
            fenetre.blit(Craie,(x_craie_3,y_craie_3))
            fenetre.blit(Craie,(x_craie_4,y_craie_4))
            fenetre.blit(Craie,(x_craie_5,y_craie_5))
            fenetre.blit(Effaceur, (x_effaceur_1,y_effaceur_1))
            fenetre.blit(Effaceur, (x_effaceur_2,y_effaceur_2))
            fenetre.blit(Livre, (x_livre_1, y_livre_1))
            fenetre.blit(Livre, (x_livre_2, y_livre_2))
            fenetre.blit(Feutre, (x_feutre_1,y_feutre_1))
            fenetre.blit(Feutre, (x_feutre_2,y_feutre_2))
            fenetre.blit(Feutre, (x_feutre_3,y_feutre_3))
            fenetre.blit(Boss, (x_boss, y_boss))
            pygame.display.flip()

    #BOUCLE GAME OVER
    while game_over:
        x_plateforme_1 = x_plateforme_1_ref_niv1
        y_plateforme_1 = y_plateforme_1_ref_niv1
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
        x_prepa_2 = x_prepa_2_ref
        x_collegien_1 = x_collegien_1_ref
        x_collegien_2 = x_collegien_2_ref
        x_collegien_3 = x_collegien_3_ref
        x_collegien_4 = x_collegien_4_ref
        x_collegien_5 = x_collegien_5_ref

        for event in pygame.event.get():
                fond_game_over = pygame.image.load(image_game_over).convert()#On charge le fond de game over
                if event.type == QUIT:
                    continuer_personnage = 0
                    continuer_jeu = 0
                    continuer_jeu2 = 0
                    game_over = 0
                    victoire=0
                    continuer = 0
                    pygame.mixer.music.stop()


                elif event.type == KEYDOWN:
                    if event.key == K_F1: # appuyer F1 pour rejouer
                        game_over = 0 #on ferme la fenetre game over
                        continuer_accueil = 0
                        continuer_personnage = 0
                        victoire=0

                    elif event.key == K_F2:#F2 pour quitter
                        game_over = 0 #on ferme la fenetre game over
                        victoire=0
                        continuer= 0 # on ferme le jeu
                fenetre.blit(fond_game_over,(0,0))
                pygame.display.flip()
                pygame.mixer.music.stop()


    #BOUCLE VICTOIRE
    while victoire:
        fond_victoire = pygame.image.load(image_victoire).convert()#On charge le fond de victoire
        for event in pygame.event.get():
                if event.type == QUIT:
                    continuer_personnage = 0
                    continuer_jeu = 0
                    continuer_jeu2 = 0
                    continuer_jeu3 = 0
                    game_over = 0
                    continuer = 0
                    victoire = 0
                    pygame.mixer.music.stop()
        if pygame.key.get_pressed()[pygame.K_ESCAPE] :#Si l'utilisateur presse Echap ici, on revient seulement au menu
                        victoire=0
        fenetre.blit(fond_victoire,(0,0))
        pygame.display.flip()
        pygame.mixer.music.stop()


pygame.quit()