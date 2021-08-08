from genieCivilOuvrage2D import * 

# Fonction pour dessiner l'etage 
def etage():
    tableau_coordonees_x = [-400, 170]
    rectangle(x=-400, y=234, longueur=800, largeur=65, fill=False)
    for i in range(2):
        rectangle(x=tableau_coordonees_x[i], y=234, longueur=230, largeur=65, fill=False)
        rectangle(x=tableau_coordonees_x[i], y=234, longueur=230, largeur=65, fill=False)

# Fonction pour dessiner le toit de l'etage
def toit_etage():
    color("#000000", "#A9D18E")
    trapeze(x=-172, y=299, petite_base=340, cote=135, grande_base=580, fill=True)
    triangle(x=170, y=300, base=230, angle1=153.4, cote=124.5, angle2=52, cote2=124.5, fill=True)
    triangle(x=-400, y=300, base=230, angle1=154.8, cote=131.9, angle2=51.8, cote2=125.5, fill=True)

# Fonction pour dessiner les portes de l'etage
def portes_etage():
    tableau_coordonnees_x = [
        -375.5, -358.5, -305.5, -288.5, -235, -218,
        198, 215, 266, 283, 334, 351, -145, -128, -77, 
        -60, -26, -9, 25, 42, 102, 119
    ]
    for i in range(len(tableau_coordonnees_x)):
        rectangle(x=tableau_coordonnees_x[i], y=234, longueur=17, largeur=45, fill=False)

# Fonction pour dessiner la devanture de la maison
def devanture_maison():
    color("#000000", "#F2F2F2")
    rectangle(x=-600, y=-300, longueur=1200, largeur=500, fill=True)
    color("#000000", "#FFFFFF")
    rectangle(x=-600, y=-300, longueur=1200, largeur=15, fill=True)
    color("#000000", "#F2F2F2")
    trapeze(x=-600, y=200, petite_base=1200, cote=80, grande_base=1343, fill=True)
    color("#000000", "#FFFFFF")
    rectangle(x=-111, y=189, longueur=213, largeur=45, fill=True)
    legende_maquette(x=-35, y=209, legende="WELCOME")

# Fonction pour dessiner les fenetres de la maison
def fenetres_devanture():
    color("#000000", "#A6A6A6")
    tableau_coordonnees_x_fenetres = [
        -570, -406, -242, 104, 268, 432
    ]
    tableau_coordonnees_x_sous_fenetres = [
        -561, -397, -233, 113, 277, 441
    ]
    for i in range(6):
        color("#000000", "#A6A6A6")
        rectangle(tableau_coordonnees_x_fenetres[i], y=-273, longueur=130, largeur=450, fill=True)
        color("#000000", "#FFFFFF")
        rectangle(tableau_coordonnees_x_sous_fenetres[i], y=-259, longueur=112, largeur=235, fill=True)
        rectangle(tableau_coordonnees_x_sous_fenetres[i], y=38, longueur=112, largeur=125, fill=True)
        rectangle(tableau_coordonnees_x_sous_fenetres[i], y=-259, longueur=56, largeur=235, fill=False)
        rectangle(tableau_coordonnees_x_sous_fenetres[i], y=-259, longueur=112, largeur=117.5, fill=False)
        rectangle(tableau_coordonnees_x_sous_fenetres[i], y=38, longueur=56, largeur=125, fill=True)
        rectangle(tableau_coordonnees_x_sous_fenetres[i], y=38, longueur=112, largeur=62.5, fill=False)

# Fonction pour dessiner un point plein
def point(x, y, size, couleur):
    penup()
    goto(x,y)
    pendown()
    dot(size, couleur)

# Fonction pour dessiner le portail
def portail_devanture():
    color("#000000", "#D9D9D9")
    rectangle(x=-83, y=-285, longueur=157, largeur=474, fill=True)
    color("#000000", "#FFFFFF")
    rectangle(x=-83, y=-285, longueur=157, largeur=76, fill=True)
    rectangle(x=-72, y=-285, longueur=134, largeur=76, fill=True)
    rectangle(x=-83, y=-209, longueur=157, largeur=11, fill=True)
    color("#000000", "#FFFFFF")
    rectangle(x=-72, y=-198, longueur=135, largeur=387, fill=True)
    color("#000000", "#D9D9D9")
    rectangle(x=-61, y=-198, longueur=113, largeur=387, fill=True)
    color("#000000", "#FFFFFF")
    rectangle(x=-42, y=-198, longueur=75, largeur=175, fill=True)
    rectangle(x=-42, y=-198, longueur=37.5, largeur=175, fill=True)
    rectangle(x=-42, y=-198, longueur=75, largeur=87.5, fill=False)
    rectangle(x=-42, y=-209, longueur=75, largeur=11, fill=True)
    rectangle(x=-48, y=-220, longueur=87, largeur=11, fill=True)
    rectangle(x=-52, y=-233, longueur=95, largeur=13, fill=True)
    rectangle(x=-56, y=-246, longueur=103, largeur=13, fill=True)
    rectangle(x=-60, y=-259, longueur=111, largeur=13, fill=True)
    rectangle(x=-64, y=-272, longueur=119, largeur=13, fill=True)
    rectangle(x=-68, y=-285, longueur=127, largeur=13, fill=True)
    demi_cercle(x=33, y=-23, radius=37.7, fill=True)
    point(x=-8, y=46, size=35, couleur='black')
    color("#000000", "#FFFFFF")
    rectangle(x=-40, y=78, longueur=64, largeur=53, fill=True)
    rectangle(x=-40, y=78, longueur=32, largeur=53, fill=False)
    rectangle(x=-83, y=-198, longueur=11, largeur=387, fill=True)
    rectangle(x=62.5, y=-198, longueur=11, largeur=387, fill=True)
    
# Fonction Principale
def programme_principal():
    setup(width=2000, height=2500, startx=0, starty=0)
    title("MY WONDERFUL HOUSE !")
    speed(15)
    pensize(2)
    devanture_maison()
    fenetres_devanture()
    portail_devanture()
    etage()
    portes_etage()
    toit_etage()
    legende_maquette(x=-85, y=-340, legende="Figure 2 : Façade d'un Batiment")

    exitonclick()

if __name__ == '__main__':
    programme_principal()