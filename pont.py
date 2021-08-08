from genieCivilOuvrage2D import *    

# Fonction pour dessiner la Portion1 du pont
def premiere_portion_pont():
    demi_ellipse(x=-25, y=0, radius=212)
    subdivision(x=-67, y=0, distance=64)
    subdivision(x=-109, y=0, distance=88)
    subdivision(x=-151, y=0, distance=98)
    subdivision(x=-193, y=0 , distance=106)
    subdivision(x=-235, y=0 , distance=98)
    subdivision(x=-277, y=0, distance=84)
    subdivision(x=-319, y=0, distance=64)
    oblique(x=-25, y=0, radius=45, orientation='rt', distance=44)
    triangle(x=-151, y=0, base=84, angle1=116.5, cote=95, angle2=127, cote2=95, fill=False)
    triangle(x=-235, y=0, base=84, angle1=112, cote=114, angle2=137, cote2=114, fill=False)
    triangle(x=-319, y=0, base=84, angle1=117, cote=95, angle2=127, cote2=95, fill=False)
    oblique(x=-361, y=0, radius=-45, orientation='lt',  distance=-44)

# Fonction pour dessiner la Portion2 du pont
def deuxieme_portion_pont():
    demi_ellipse(x=309, y=0, radius=212)
    subdivision(x=267, y=0, distance=64)
    subdivision(x=225, y=0, distance=88)
    subdivision(x=183, y=0, distance=98)
    subdivision(x=141, y=0, distance=106)
    subdivision(x=99, y=0, distance=98)
    subdivision(x=57, y=0, distance=84)
    subdivision(x=15, y=0, distance=64)
    oblique(x=309, y=0, radius=45, orientation='rt', distance=44)
    triangle(x=183, y=0, base=84, angle1=116.5, cote=95, angle2=127, cote2=95, fill=False)
    triangle(x=99, y=0, base=84, angle1=112, cote=114, angle2=137, cote2=114, fill=False)
    triangle(x=15, y=0, base=84, angle1=117, cote=95, angle2=127, cote2=95, fill=False)
    oblique(x=-25.2, y=0, radius=-45, orientation='lt',  distance=-42.4)

# Fonction pour dessiner la Portion3 du pont
def troisieme_portion_pont():
    demi_ellipse(x=643, y=0, radius=212)
    subdivision(x=601, y=0, distance=64)
    subdivision(x=559, y=0, distance=88)
    subdivision(x=517, y=0, distance=98)
    subdivision(x=475, y=0, distance=106)
    subdivision(x=433, y=0, distance=98)
    subdivision(x=391, y=0, distance=84)
    subdivision(x=349, y=0, distance=64)
    oblique(x=643, y=0, radius=45, orientation='rt', distance=44)
    triangle(x=517, y=0, base=84, angle1=116.5, cote=95, angle2=127, cote2=95, fill=False)
    triangle(x=433, y=0, base=84, angle1=112, cote=114, angle2=137, cote2=114, fill=False)
    triangle(x=349, y=0, base=84, angle1=117, cote=95, angle2=127, cote2=95, fill=False)
    oblique(x=307, y=0, radius=-45, orientation='lt',  distance=-42.4)

# Fonction pour dessiner les Pieds du pont
def pieds_pont():
    home()
    color("#0070c0", "#0070c0")
    tableau_coordonnees_x_petit_pieds = [-67, 267]
    tableau_coordonnees_x_grand_pieds = [-88, 246]
    for i in range(2):
        rectangle(x=tableau_coordonnees_x_petit_pieds[i],y=-19.5, longueur=84, largeur=20, fill=True)
        rectangle(x=tableau_coordonnees_x_grand_pieds[i],y=-39, longueur=126, largeur=20, fill=True)

# Fonction principale
def programme_principal():
    setup(width=2000, height=2500, startx=0, starty=0)
    title("MY WONDERFUL BRIDGE !")
    speed(8)
    shape("turtle")
    pencolor("#4976c6")
    pensize(3.5)
    premiere_portion_pont()
    deuxieme_portion_pont()
    troisieme_portion_pont()
    pieds_pont()
    shape('classic')
    pencolor("#000000")
    legende_maquette(x=50, y=-100, legende="Figure 1 : Maquette d'un Pont")

    exitonclick()

if __name__ == '__main__':
    programme_principal()
    

