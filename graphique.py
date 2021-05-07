import numpy as np
import matplotlib.pyplot as plt
import math

class Graphique:
    def __init__(self, abscisse, ordonnee, nom_abscisse, nom_ordonnee, titre):
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        self.nom_abscisse = nom_abscisse
        self.nom_ordonnee = nom_ordonnee
        self.titre = titre
        
    def affichage_graphique(self):
        plt.plot(self.abscisse, self.ordonnee, 'r')
        plt.title(self.titre)
        plt.xlabel(self.nom_abscisse)
        plt.ylabel(self.nom_ordonnee) 
        plt.show()   
    
test = Graphique(abs, ord, 'x', 'y', 'titre') 

Graphique.affichage_graphique(test)
