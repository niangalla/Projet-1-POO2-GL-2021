from turtle import *
""" Module spécialise en dessin de formes et figures géométriques pour créer des structures
    en Génie Civil comme des Ponts, des Maisons ect. avec la bibliothéque Python TURTLE 
"""

# Fonction pour dessiner un cercle
""" Entrées : radius , coordonnées x et y, fill(boolean pour colorier)
    Sorties :-
    Méthode : usage de la fonction circle de Turtle
    Connu :-
 """
def cercle(x, y, radius, fill):
    penup()
    goto(x,y)
    pendown()
    if(fill):
        color('black', 'black')
        begin_fill()
        circle(radius)
        end_fill()
    else:
        circle(radius)

# Fonction pour dessiner un demi-cercle
""" Entrées : radius, coordonnées x et y, fill(boolean pour colorier)
    Sorties :-
    Méthode : usage de la fonction circle de Turtle et d'un angle de 180
    Connu :-
 """
def demi_cercle(x, y, radius, fill):
    pensize(2.49)
    penup()
    goto(x,y)
    pendown()
    seth(90)
    if(fill):
        color("#000000", "#D9D9D9")
        begin_fill()
        circle(radius, 180)
        end_fill()
    else:
        circle(radius, 180)
    seth(0)

# Fonction pour dessiner un carré
""" Entrées : cote, coordonnées x et y
    Sorties :-
    Méthode : usage d'une boucle , de deplacement forward et d'un angle de 90
    Connu :-
 """
def carre(x, y, cote):
    penup()
    goto(x,y)
    pendown()
    for i in range(4):
        forward(cote)
        left(90)

# Fonction pour dessiner un triangle
""" Entrées : base, angle1, cote, angle2, cote2, fill(boolean pour colorier), coordonnées x et y
    Sorties :-
    Méthode : usage des fonctions forward et left de Turtle
    Connu :-
 """
def triangle(x,y, base, angle1, cote, angle2, cote2, fill):
    penup()
    goto(x,y)
    pendown()
    seth(0)
    if(fill):
        begin_fill()
        fd(base)
        lt(angle1)
        fd(cote)
        lt(angle2)
        fd(cote2)
        end_fill()
    else:
        fd(base)
        lt(angle1)
        fd(cote)
        lt(angle2)
        fd(cote2)
    up()


# Fonction pour dessiner un rectangle
""" Entrées : longueur,largeur coordonnées x et y, fill(boolean pour colorier)
    Sorties :-
    Méthode : usage des fonctions forward et left de Turtle
    Connu :-
 """
def rectangle(x, y, longueur, largeur, fill):
    penup()
    goto(x,y)
    pendown()
    if (fill):
        # color("#0E4BEF", "#0E4BEF")
        begin_fill()
        for i in range(4):
            if(i % 2 == 0):
                fd(longueur)
                lt(90)
            else:
                fd(largeur)
                lt(90)
        end_fill()
    else:
        for i in range(4):
            if(i % 2 == 0):
                fd(longueur)
                lt(90)
            else:
                fd(largeur)
                lt(90)

# Fonction pour dessiner un polygone
""" Entrées : nombre_cote, longeur_cote, coordonnées x et y
    Sorties :-
    Méthode : usage des fonctions forward et left de Turtle
    Connu :-
 """
def polygone(x, y, nombre_cote, longueur_cote):
    for i in range(nombre_cote):
        fd(longueur_cote)
        lt(360/nombre_cote)

# Fonction pour dessiner une trapeze
""" Entrées : petite_base, cote, grande_base, fill(boolean pour colorier), coordonnées x et y
    Sorties :-
    Méthode : usage des fonctions forward et left de Turtle
    Connu :-
 """
def trapeze(x,y, petite_base, cote, grande_base, fill):
    # begin_poly()
    penup()
    goto(x,y)
    pendown()
    if(fill):
        begin_fill()
        for i in range(1): 
            fd(petite_base)
            lt(25)
            fd(cote)
            lt(155)
            fd(grande_base)
            lt(155)
            fd(cote)
        seth(0)
        end_fill()
    else:
        for i in range(1): 
            fd(petite_base)
            lt(25)
            fd(cote)
            lt(155)
            fd(grande_base)
            lt(155)
            fd(cote)
        seth(0)

# Fonction pour dessiner un losange
""" Entrées : long, coordonnées x et y
    Sorties :-
    Méthode : usage des fonctions forward et left de Turtle
    Connu :-
 """
def losange(x,y, long):
    penup()
    goto(x,y)
    pendown()
    seth(120)
    for i in range(2):
        fd(long)
        lt(120)
        fd(long)
        lt(60)

# Fonction pour dessiner une ellipse complete
""" Entrées : radius, coordonnées x et y
    Sorties :-
    Méthode : usage de la fonction circle de Turtle
    Connu :-
 """
def ellipse_complete(x, y, radius):
    penup()
    goto(x,y)
    pendown()
    for i in range(2):
        circle(radius, 90)
        circle(radius//4, 90)

# Fonction pour dessiner une demie-ellipse
""" Entrées : radius, coordonnées x et y
    Sorties :-
    Méthode : usage de la fonction circle de Turtle
    Connu :-
 """
def demi_ellipse(x, y, radius):
    penup()
    goto(x,y)
    pendown()
    for i in range(1):
        seth(90)
        circle(60, 45)
        circle(radius, 90)
        circle(60, 45)
        seth(0)
        fd(336)

# Fonction pour subdiviser les pont
""" Entrées : distance, coordonnées x et y
    Sorties :-
    Méthode : usage des fonctions forward, left et back de Turtle
    Connu :-
 """
def subdivision(x, y, distance):
    goto(x,y)
    lt(90)
    fd(distance)
    back(distance)
    rt(90)

# Fonction pour dessiner un trai oblique
""" Entrées : radius, coordonnées x et y, orientation, distance
    Sorties :-
    Méthode : usage de la fonction circle de Turtle et de forward
    Connu :-
 """
def oblique(x,y, radius, orientation, distance):
    goto(x,y)
    seth(90)
    up()
    circle(radius, 45)
    if(orientation == 'rt'):
        lt(94)
    else:
        if(orientation == 'lt'):
            lt(87)
    down()
    fd(distance)
    up()

# Fonction pour ecrire la légende de la maquette maison et celle du pont
""" Entrées : legende, coordonnées x et y
    Sorties :-
    Méthode : usage de la fonction write de Turtle pour ecrire du texte
    Connu :-
 """
def legende_maquette(x, y, legende):
    pensize(2)
    up()
    goto(x,y)
    down()
    write(legende, True)
