import turtle
import random

# Configuration de la fenêtre graphique
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Devoir L2 - Feux d'artifice géométriques")

# Configuration de la tortue principale
t = turtle.Turtle()
t.speed(0)  # Vitesse maximale pour un dessin instantané
t.width(2)

# Liste de couleurs vibrantes pour les explosions
couleurs = ["cyan", "magenta", "yellow", "orange", "lime", "pink", "turquoise", "gold"]

def dessiner_feu_artifice(x, y, rayon_max):
    """Fonction pour dessiner un feu d'artifice à une position (x, y) donnée"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Choix d'une couleur aléatoire pour ce feu d'artifice
    couleur_actuelle = random.choice(couleurs)
    t.color(couleur_actuelle)
    
    # Dessin des rayons superposés (effet d'explosion)
    for _ in range(36):
        t.forward(rayon_max)
        t.backward(rayon_max)
        t.left(10)  # 36 * 10 = 360 degrés (cercle complet)

# Génération de plusieurs explosions de feux d'artifice à des endroits aléatoires
positions = [(-150, 100), (150, 120), (0, -50), (-100, -100), (120, -80)]

for pos in positions:
    dessiner_feu_artifice(pos[0], pos[1], rayon_max=90)

# Message de fin ou maintien de la fenêtre
t.hideturtle()
turtle.done()